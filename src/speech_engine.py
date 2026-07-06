# src/speech_engine.py
import os
import uuid
from gtts import gTTS
from config import Config

def generate_audio(text, language_name):
    """
    Synthesizes speech from translated text and saves it securely 
    as an ephemeral audio artifact.
    """
    if not text.strip():
        return None
        
    lang_code = Config.TTS_LANG_CODES.get(language_name, "en")
    
    # Generate unique filename to prevent enterprise concurrency clashes
    filename = f"{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(Config.TEMP_AUDIO_DIR, filename)
    
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(filepath)
        return filepath
    except Exception as e:
        raise RuntimeError(f"Speech synthesis failed: {str(e)}")