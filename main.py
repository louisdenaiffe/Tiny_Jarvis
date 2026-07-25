import speaker  # Loads the pyaudio engine
import listener # Same here, this will initialize listener.py once
from transcriber import transcribe_audio
from OLED import AssistantDisplay
from ai import generate, sentence_buffer
from cooking.cooking_helper import get_recipe, format_cooking_sentence
import os
import time


def main():
    d = AssistantDisplay()
    listener.init_listener()
    if not os.path.exists("recordings"):  # small check in case recordings/ dir doesnt exist, you never know
        print("Warning: you didn't have a recordings/ folder, so we created one")
        os.makedirs("recordings")
    print("Tiny Jarvis is active and listening!")
    d.show_image("home.png")
    while True:
        audio_file = listener.get_latest_recordings()
        if audio_file:  # if audio recordings are found in recordings/
            try:
                print(f"Found new recording: {audio_file}")
                print("Transcribing audio...")
                prompt = transcribe_audio(audio_file)  # fast-whisper at work turning that .wav file into text
                print(f"Prompt : {prompt}")
                if not prompt.strip():  # if the user didn't say anything, if faster-whisper returned nothing
                    print("Empty transcription. Skipping.")
                    continue # skips the rest of the code in this iteration and goes back to the top of the while loop
                if prompt.startswith("Cooking"):
                    recipe_object = get_recipe()
                    d.show_text(recipe_object['Ingredients'])
                    raw_token_stream = [format_cooking_sentence(recipe_object)]  # we put it in a list so sentence_buffer can iterate over it without breaking
                else:
                    print("Generating response...")
                    d.show_image("thinking_animation.gif")
                    raw_token_stream = generate(prompt)  # the raw token stream generated in real time by the ai chatbot
                sentence_stream = sentence_buffer(raw_token_stream)  # we "filter" that raw token stream into a list of sentences
                speech_success = speaker.speak(sentence_stream)  # that list/stream of sentences is poured into the speakers!
                if not speech_success:
                    print("Failed to stream speech")
            except Exception as e:  # to catch any errors at any time in the process
                print(f"[ERROR IN PIPELINE]: {e} ")
            finally:  # whether the "try" or "except" blocks was executed, this will run in the "if audio_file" block
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    print("Deleted recording file")
                    d.show_image("home.png")
        time.sleep(0.2)  # wait a bit in between calling get_latest_recordings()


if __name__ == "__main__":
    main()