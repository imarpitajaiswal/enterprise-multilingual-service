# config.py
import os

class Config:
    # We will use MarianMT models from HuggingFace for rapid, offline translation
    # Example: English to Hindi, English to French
    SUPPORTED_LANGUAGES = {
        "Hindi": "Helsinki-NLP/opus-mt-en-hi",
        "French": "Helsinki-NLP/opus-mt-en-fr",
        "Spanish": "Helsinki-NLP/opus-mt-en-es",
        "German": "Helsinki-NLP/opus-mt-en-de"
    }
    
    # gTTS language codes mapping
    TTS_LANG_CODES = {
        "Hindi": "hi",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "English": "en"
    }
    
    TEMP_AUDIO_DIR = "temp"
    os.makedirs(TEMP_AUDIO_DIR, exist_ok=True)