import whisper

def transcribe_audio(audio_path: str, language: str = "hi") -> str:
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language=language)
    return result['text']
