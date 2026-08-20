#!/bin/bash
set -e

# Parse flags
SKIP_MODEL=false
AUTO_REBOOT=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-model)
            SKIP_MODEL=true
            shift
            ;;
        --reboot)
            AUTO_REBOOT=true
            shift
            ;;
        --help|-h)
            echo "Usage: ./install.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --skip-model    Skip downloading the AI model and Piper voice"
            echo "  --reboot        Auto-reboot if I2C was newly enabled"
            echo "  --help, -h      Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Run './install.sh --help' for usage."
            exit 1
            ;;
    esac
done

echo "=========================================="
echo "  Tiny Jarvis Installer"
echo "=========================================="

# Check if running on Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then
    echo "WARNING: This doesn't appear to be a Raspberry Pi."
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

I2C_WAS_ENABLED=false

echo ""
echo "[1/10] Installing system dependencies..."
sudo apt update
sudo apt install -y \
    git \
    python3 \
    python3-venv \
    python3-dev \
    python3-pip \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff6-dev \
    libportaudio2 \
    portaudio19-dev \
    cmake \
    build-essential \
    wget \
    librespot \
    swig \
    liblgpio-dev 

echo ""
echo "[2/10] Checking GPU memory allocation..."
GPU_MEM=$(vcgencmd get_mem gpu | cut -d= -f2 | cut -dM -f1)
if [ "$GPU_MEM" -gt 16 ]; then
    echo "WARNING: GPU memory is ${GPU_MEM}M. For best performance, set gpu_mem=16 in /boot/firmware/config.txt"
    echo "Current setting: $(vcgencmd get_mem gpu)"
fi

echo ""
echo "[3/10] Enabling I2C interface..."
if ! grep -q "^dtparam=i2c_arm=on" /boot/firmware/config.txt 2>/dev/null; then
    echo "dtparam=i2c_arm=on" | sudo tee -a /boot/firmware/config.txt > /dev/null
    echo "I2C enabled in config.txt. Reboot required for full effect."
    I2C_WAS_ENABLED=true
else
    echo "I2C already enabled."
fi
sudo modprobe i2c-dev 2>/dev/null || true

echo ""
echo "[4/10] Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo ""
echo "[5/10] Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "[6/10] Installing llama-cpp-python with ARM optimizations..."
echo "This will take 10-30 minutes. Grab a coffee."
CMAKE_ARGS="-DLLAMA_NATIVE=ON -DLLAMA_ARM_ARCH=armv8.4-a" \
    pip install llama-cpp-python --no-cache-dir

echo ""
echo "[7/10] Setting up performance mode..."
sudo tee /etc/systemd/system/cpu-performance.service > /dev/null << 'EOF'
[Unit]
Description=Set CPU governor to performance
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now cpu-performance

echo ""
echo "[8/10] Creating necessary directories..."
mkdir -p models piper_voices recordings

echo ""
echo "[9/10] Setting up Tiny Jarvis as a systemd service..."

PROJECT_DIR=$(pwd)
USER_NAME=$(whoami)

sudo tee /etc/systemd/system/tiny-jarvis.service > /dev/null << EOF
[Unit]
Description=Tiny Jarvis - Local offline voice AI agent
After=network.target sound.target
Wants=network.target

[Service]
Type=simple
User=${USER_NAME}
Group=${USER_NAME}
WorkingDirectory=${PROJECT_DIR}
Environment=PATH=${PROJECT_DIR}/.venv/bin:/usr/local/bin:/usr/bin:/bin
Environment=PYTHONUNBUFFERED=1
Environment=HOME=/home/${USER_NAME}
ExecStart=${PROJECT_DIR}/.venv/bin/python ${PROJECT_DIR}/main.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable tiny-jarvis.service

echo "  -> Service created: tiny-jarvis.service"
echo "  -> Start it now:    sudo systemctl start tiny-jarvis"
echo "  -> Check status:    sudo systemctl status tiny-jarvis"
echo "  -> View logs:       sudo journalctl -u tiny-jarvis -f"

echo ""
echo "[10/10] Downloading AI model and Piper voice..."

if [ "$SKIP_MODEL" = true ]; then
    echo "  -> Skipping model download (--skip-model flag set)"
else
    echo "  -> Downloading Llama 3.2 3B (Q4_K_M) ~2GB..."
    wget -q --show-progress -P models/ \
        https://huggingface.co/osmapi/Nidum-Llama-3.2-3B-Uncensored-GGUF/resolve/main/model-Q4_K_M.gguf \
        || echo "WARNING: Model download failed. Download manually from: https://huggingface.co/osmapi/Nidum-Llama-3.2-3B-Uncensored-GGUF"

    echo "  -> Downloading Piper voice..."
    python -m piper.download_voices en_US-lessac-medium \
        || echo "WARNING: Piper voice download failed. Run manually: python -m piper.download_voices en_US-lessac-medium"
fi

echo ""
echo "=========================================="
echo "  Installation complete!"
echo "=========================================="
echo ""
echo "Quick commands:"
echo "  Start service:     sudo systemctl start tiny-jarvis"
echo "  Stop service:      sudo systemctl stop tiny-jarvis"
echo "  Check status:      sudo systemctl status tiny-jarvis"
echo "  View logs:         sudo journalctl -u tiny-jarvis -f"
echo "  Disable auto-start: sudo systemctl disable tiny-jarvis"
echo ""
echo "Manual run (for testing):"
echo "  source .venv/bin/activate"
echo "  python main.py"

if [ "$I2C_WAS_ENABLED" = true ]; then
    echo ""
    echo "NOTE: I2C was newly enabled. A reboot is required for OLED to work."
    if [ "$AUTO_REBOOT" = true ]; then
        echo ""
        echo "Auto-rebooting in 10 seconds... (Ctrl+C to cancel)"
        sleep 10
        sudo reboot
    else
        echo "Reboot with: sudo reboot"
    fi
fi