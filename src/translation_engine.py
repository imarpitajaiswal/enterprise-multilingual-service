# src/translation_engine.py
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
from config import Config
import streamlit as st

@st.cache_resource # Caching prevents reloading massive tensors into memory on every UI click
def load_translation_model(language_name):
    """Loads the specific MarianMT model and tokenizer for the target language."""
    model_name = Config.SUPPORTED_LANGUAGES.get(language_name)
    if not model_name:
        raise ValueError(f"Translation to {language_name} is not currently supported.")
    
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def detect_input_language(text):
    """Detects the source language of the input text."""
    try:
        return detect(text)
    except:
        return "unknown"

def translate_text(text, target_language):
    """Executes the deep learning translation pipeline."""
    if not text.strip():
        return ""
        
    tokenizer, model = load_translation_model(target_language)
    
    # Tokenize and translate
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    
    return translated_text