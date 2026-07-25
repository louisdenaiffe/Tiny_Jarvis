from piper import PiperVoice
import pyaudio  # basically a python wrapper for the C library portaudio
import os


VOICE_PATH = "piper_voices/en_US-lessac-medium.onnx"
voice = None
try:
    p = pyaudio.PyAudio()
except:
    print("Couldn't load the pyaudio engine.")


def get_voice():
    global voice
    if voice is None:
        if not os.path.exists(VOICE_PATH):
            raise FileNotFoundError(f"Piper voice model missing at '{VOICE_PATH}'")
        voice = PiperVoice.load(VOICE_PATH)
    return voice


def speak(text):
    stream = None
    try:
        v = get_voice()
        with p.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = v.config.sample_rate,
            output = True
        ) as stream:
            for sentence in text:
              if not sentence.strip():
                  continue
              for audio_bytes in v.synthesize_stream(sentence):
                  stream.write(audio_bytes)
        return True
    except Exception as e:
        print(f"Speaker error: {e}")
        return False