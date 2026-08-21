import firmware.speaker as speaker  # Loads the pyaudio engine
import firmware.listener as listener # Same here, this will initialize listener.py once
from firmware.transcriber import transcribe_audio
from firmware.OLED import AssistantDisplay
from firmware.ai import generate, sentence_buffer
from firmware.cooking.cooking_helper import load_recipes, handle_cooking
from firmware.timer import handle_timer
from firmware.music import handle_music
import os
import time
import random


def main():
    d = initialize()
    try:
        while True:
            audio_file = listener.get_latest_recordings()
            if not audio_file:  # if audio recordings are found in recordings/
                time.sleep(0.2)
                continue
            process_recording(audio_file, d)

    except KeyboardInterrupt:
        print("Terminating this program...")

    finally:
        d.stop()
        listener.shutdown()
        

def initialize():
    d = AssistantDisplay()
    listener.init_listener()
    ensure_recordings_folder()
    load_recipes()
    print("Tiny Jarvis is active and listening!")
    d.show_metrics()
    return d


def process_recording(audio_file, d):
    try:
        print(f"Found new recording: {audio_file}")
        print("Transcribing audio...")
        prompt = transcribe_audio(audio_file)
        print(f"Prompt : {prompt}")

        if not prompt.strip():
            print("Empty transcription. Skipping.")
            return
        
        sentence_stream = handle_prompt(prompt, d)

        if sentence_stream:
            speech_success = speaker.speak(sentence_stream)

            if not speech_success:
                print("Failed to stream speech")

    except Exception as e:
        print(f"[ERROR IN PIPELINE]: {e} ")

    finally:
        cleanup_recording(audio_file, d)


def ensure_recordings_folder():
    if not os.path.exists("recordings"):  # small check in case recordings/ dir doesnt exist, you never know
            print("Warning: you didn't have a recordings/ folder, so we created one")
            os.makedirs("recordings")


def handle_prompt(prompt, d):
    if prompt.lower().startswith("cooking"):
        return handle_cooking(d)
    if prompt.lower().startswith("set a timer of"):
        return handle_timer(prompt, d)
    if prompt.lower().startswith("play"):
        return handle_music(prompt, d)
    if prompt.lower().startswith("flip"):
        return random.choice(["Heads", "Tails"])
    return handle_ai(prompt, d)


def handle_ai(prompt, d):
    print("Generating response...")
    d.show_image("thinking_animation.gif")
    raw_token_stream = generate(prompt)
    return sentence_buffer(raw_token_stream)


def cleanup_recording(audio_file, d):
    if os.path.exists(audio_file):
        os.remove(audio_file)
        print("Deleted recording file")


if __name__ == "__main__":
    main()