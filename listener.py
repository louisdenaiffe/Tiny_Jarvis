import time
import os
from scipy.io import wavfile
import numpy as np
import queue
import subprocess
from speaker import speak


try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
except Exception as e:
    print(f"Couldn't initalize sounddevice library... {e}")
    SOUNDDEVICE_AVAILABLE = False


try:
    from gpiozero import Button
    btn_a = Button(12)
    btn_b = Button(13, hold_time = 2)
    GPIO_AVAILABLE = True
except Exception as e:
    print("GPIO initialization failed. {e}. Buttons disabled.")
    GPIO_AVAILABLE = False


sample_rate = 44100
output_dir = "recordings"
audio_frames = []
is_recording = False
audio_stream = None
finished_recordings = queue.Queue()


def audio_callback(indata, frames, time, status): # sounddevice library strictly expects callback function to have four arguments
    audio_frames.append(indata.copy())


def start_recording():
    global is_recording, audio_frames, audio_stream
    if is_recording:
        return
    try:
        is_recording = True
        audio_frames = []
        audio_stream = sd.InputStream(samplerate = sample_rate, channels=1, callback=audio_callback)
        audio_stream.start()
    except Exception as e:
        print(f"Failed to start recording: {e}")
        is_recording = False


def stop_recording():
    global is_recording, audio_stream
    filename = None
    if not is_recording:
        return
    try:
        if audio_stream:
            audio_stream.stop()
            audio_stream.close()
            audio_stream = None
        if audio_frames:
            full_audio = np.concatenate(audio_frames, axis = 0)
            filename = os.path.join(output_dir, f"{int(time.time())}.wav")
            wavfile.write(filename, sample_rate, full_audio)
            finished_recordings.put(filename)
    except Exception as e:
        print(f"Error saving recording: {e}")
    finally:
        is_recording = False
    return filename


def get_latest_recordings():
    try:
        return finished_recordings.get_nowait()
    except queue.Empty:
        return None


def safe_shutdown():
    print("Shutdown button held, safely powering off rpi5")
    try:
        subprocess.run(["sudo", "poweroff"], check=True)
    except subprocess.CalledProcessError :
        print("Necessary permissions missing to run sudo poweroff... read the recommendation in README.md")
        try:
            speak(["Failed to shutdown... Have you read the recommendation in the README.md?"])
        except:
            print("Speaker unavailable")


def init_listener():
    if GPIO_AVAILABLE and SOUNDDEVICE_AVAILABLE:
        btn_a.when_pressed = start_recording
        btn_a.when_released = stop_recording
        btn_b.when_held = safe_shutdown
        print("GPIO listeners attached")
    elif not GPIO_AVAILABLE:
        print("GPIO not available. Button input disabled.")


def shutdown():
    global is_recording, audio_stream
    print("Shutting down listener...")

    if audio_stream:
        try:
            audio_stream.stop()
            audio_stream.close()
        except Exception as e:
            print(f"Error closing audio stream: {e}")
        finally:
            audio_stream = None

    is_recording = False