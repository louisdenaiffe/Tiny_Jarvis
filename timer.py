import re
import threading
from word2number import w2n
import speaker
import time


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
        timer = threading.Thread(
            target=run_timer,
            args=(minutes, d),
            daemon=True
        )
        timer.start()
        return [f"Timer started for {minutes} minutes"]
    return ["Sorry, I couldn't quite catch that."]


def run_timer(minutes, d):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        d.show_text(f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        total_seconds -= 1
    timer_finished(minutes, d)


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
