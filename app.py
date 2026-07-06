# app.py
import streamlit as st
import os
from config import Config
from src.translation_engine import translate_text, detect_input_language
from src.speech_engine import generate_audio

# 1. UI Configuration
st.set_page_config(
    page_title="Multilingual Microservice", 
    page_icon="🌍", 
    layout="wide"
)

st.title("🌍 Global Multilingual Communications API")
st.markdown("### Enterprise-Grade Neural Translation & Speech Synthesis")
st.divider()

# 2. Pipeline Layout
col1, col2 = st.columns(2)

with col1:
    st.header("Source Communications")
    source_text = st.text_area(
        "Input Corporate Messaging:", 
        height=250, 
        placeholder="Enter text to localize for regional deployment..."
    )
    
    if source_text:
        detected_lang = detect_input_language(source_text)
        st.caption(f"Detected Source Language Code: `{detected_lang.upper()}`")

with col2:
    st.header("Localization Output")
    target_language = st.selectbox(
        "Select Target Region:", 
        list(Config.SUPPORTED_LANGUAGES.keys())
    )
    
    if st.button("Execute Localization Pipeline", type="primary", use_container_width=True):
        if source_text:
            try:
                # Stage 1: Neural Translation
                with st.spinner(f"Processing Neural Translation to {target_language}..."):
                    translated_text = translate_text(source_text, target_language)
                    
                st.success("Translation Complete.")
                st.text_area("Localized Messaging:", value=translated_text, height=120)
                
                # Stage 2: Audio Artifact Generation
                with st.spinner("Synthesizing Voice Artifact..."):
                    audio_path = generate_audio(translated_text, target_language)
                    
                    if audio_path and os.path.exists(audio_path):
                        st.audio(audio_path, format="audio/mp3")
                        
                        # Enterprise download artifact
                        with open(audio_path, "rb") as file:
                            st.download_button(
                                label="📥 Download Audio Artifact (.mp3)",
                                data=file,
                                file_name=f"corporate_broadcast_{target_language.lower()}.mp3",
                                mime="audio/mp3",
                                use_container_width=True
                            )
            except Exception as e:
                st.error(f"Pipeline Failure: {str(e)}")
        else:
            st.warning("Please provide source text to initiate the pipeline.")