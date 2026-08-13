# TINY JARVIS

## Table of contents:

 - [Description](#description)
    - [Quick description](#quick-description)
    - [Project structure](#project-structure)
    - [Application and user scenario](#application-and-user-scenario)
 - [How to install](#how-to-install)
    - [Prerequisites](#prerequisites)
    - [Dependencies](#dependencies-run-these-in-order)
 - [Hardware](#hardware)

# Description

## Quick description

Tiny Jarvis is a local, offline voice-controlled AI Agent that runs directly on your [Raspberry pi 5](https://www.raspberrypi.com/).\
The software for Tiny Jarvis is all in this repository, and you can take a look at the hardware [here](#hardware).

> Note: this project is still in heavy development. As such I would not recommend installing it just yet. 

## Project structure
```
Tiny_Jarvis/
├── .venv/  # virtual env with all dependencies installed
├── pcb/
├── piper_voices/
├── models/
├── recordings/
├── assets/
├── ai.py
├── listener.py
├── main.py  # the main script
├── OLED.py
├── speaker.py
├── transcriber.py
├── README.md
└── requirements.txt
```
## Application and User Scenario

The OLED screen shows an `IDLE` animation when idle.\
User presses a button, gives a command, and releases the button when done speaking.\
The captured audio is translated into text by [faster-whisper](https://pypi.org/project/faster-whisper/0.3.0/).
That text is given as a prompt to a model of your choice using [llama.cpp](https://github.com/abetlen/llama-cpp-python) (optimized for Raspberry pi 5), preferably a low-parameter model like Llama-3.2-3B, balancing speed and quality.\
The model's ouput is streamed into [Piper TTS](https://github.com/rhasspy/piper), a text-to-speech model, and played through the speakers (stereo sound).\
OLED screen display a variety of animations meanwhile.\
The other button serves a single purpose: to turn off the Raspberry Pi 5 safely through `sudo poweroff`.


**Features:**
 - "Play ..." --> Tiny_Jarvis will search a free online music database for that query using Mopidy and stream the music through the speakers. (Still in development, and only works when connected to wi-fi)
 - "Cooking ..." --> Tiny_Jarvis will output a random recipe from a list, display the ingredients, and read the recipe out loud.
 - "Set a timer of ... minutes" --> Tiny_Jarvis will set a timer for the needed time, and display it in real time on the OLED screen.


# How to install

## Prerequisites

<b>OS recommendation:</b> Raspberry Pi OS Lite (64-bit)

Before doing anything, clone the repo:
```bash
sudo apt update
sudo apt install git
git clone https://github.com/LouisD2008/Tiny_Jarvis.git
```

## Dependencies:

Run the `install.sh` script by running:
```bash
chmod +x install.sh
./install.sh
```
You may of course choose a different AI model if you wish, but this is the current recommended one for a Raspberry Pi 5.\
Feel free as well to choose a different Piper TTS voice!

For the second button to work flawlessly, I would recommend editing the `/etc/sudoers` file by running 
```bash
sudo visudo
```
then add this at the bottom, replacing `username` with your username:
```bash
username ALL=(ALL) NOPASSWD: /sbin/poweroff, /sbin/reboot
```

# Hardware

See [JOURNAL.md](JOURNAL.md)

Check out the PCB files in `pcb/`.