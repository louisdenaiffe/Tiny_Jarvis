from faster_whisper import WhisperModel
model = WhisperModel(
    "tiny", 
    device="cpu", 
    compute_type="int8",
    cpu_threads=4   # for rpi5
    )


def transcribe_audio(file):
    segments, info = model.transcribe(file, beam_size = 1)
    transcription = ""
    for segment in segments:
        transcription = transcription + segment.text
    return transcription.strip()