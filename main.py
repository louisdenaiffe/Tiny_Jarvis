import speaker  # Loads the pyaudio engine
import listener # Same here, this will initialize listener.py once
from transcriber import transcribe_audio
from OLED import AssistantDisplay
from ai import generate, sentence_buffer
from cooking.cooking_helper import get_random_recipe, load_recipes, format_cooking_sentence
import os
import time
from word2number import w2n
import re
import threading


def main():
    d = initialize()
    while True:
        audio_file = listener.get_latest_recordings()
        if not audio_file:  # if audio recordings are found in recordings/
            time.sleep(0.2)
            continue
        process_recording(audio_file, d)


def initialize():
    d = AssistantDisplay()
    listener.init_listener()
    ensure_recordings_folder()
    load_recipes()
    print("Tiny Jarvis is active and listening!")
    d.show_image("home.png")
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
    if prompt.startswith("Cooking"):
        return handle_cooking(d)
    if prompt.startswith("Set a timer of"):
        return handle_timer(prompt, d)
    if prompt.startswith("Play"):
        return handle_music(prompt, d)
    
    return handle_ai(prompt, d)


def handle_cooking(d):
    recipe = get_random_recipe()
    d.show_text(recipe['Ingredients'])
    return [format_cooking_sentence(recipe)]


def handle_timer(prompt, d):
    normalized_prompt = normalize_number(prompt)
    match = re.match(
        r"^Set a timer of (\d+) minutes$",
        normalized_prompt,
        re.IGNORECASE
        )
    if match:
        minutes = int(match.group(1))
        d.show_text(f"{minutes} min")
        timer = threading.Timer(
            minutes * 60,
            timer_finished,
            args=[minutes, d]
        )
        timer.start()
        return [f"Timer started for {minutes} minutes"]
    return ["Sorry, I couldn't quite catch that."]


def timer_finished(minutes, d):
    print(f"Timer finished: {minutes} minutes")
    d.show_text("TIMER DONE!")
    speaker.speak([
        f"Your {minutes} minute timer is finished."
    ])

def normalize_number(text):
    words = text.split()
    result = []
    number_words = []
    for word in words:
        clean = re.sub(r"[^a-zA-Z]", "", word)
        try:
            w2n.word_to_num(" ".join(number_words + [clean]))
            number_words.append(clean)
        except ValueError:
            if number_words:
                result.append(str(w2n.word_to_num(" ".join(number_words))))
                number_words = []
            result.append(word)
    if number_words:
        result.append(str(w2n.word_to_num(" ".join(number_words))))
    return " ".join(result)


def handle_music(prompt, d):
    ...


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