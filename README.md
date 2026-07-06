# 🌍 Global Multilingual Communications API

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![MIT](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

Global Multilingual Communications API is a multilingual translation application built with **Hugging Face Transformers**, **MarianMT**, **PyTorch**, and **Streamlit**.

The application translates text between multiple languages using locally executed neural machine translation models and can generate spoken audio using Google Text-to-Speech (gTTS).

The project demonstrates multilingual NLP workflows while minimizing reliance on external translation APIs.

---

## ✨ Features

- Multi-language text translation
- Local MarianMT inference
- Automatic language detection
- Audio generation using gTTS
- Interactive Streamlit interface
- Download translated audio
- Modular architecture

---

## 🏗 Architecture

```
User Input
      │
      ▼
Language Detection
      │
      ▼
SentencePiece Tokenizer
      │
      ▼
MarianMT Translation Model
      │
      ▼
Translated Text
      │
      ├────────► Display in UI
      │
      ▼
gTTS Audio Generation
      │
      ▼
Download MP3
```

---

## 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| NLP | Hugging Face Transformers |
| Translation Model | MarianMT |
| Deep Learning | PyTorch |
| Tokenizer | SentencePiece |
| Language Detection | langdetect |
| Speech | gTTS |
| Frontend | Streamlit |

---

## 📂 Project Structure

```
enterprise-multilingual-service/

├── app.py
├── requirements.txt
├── translator.py
├── temp/
├── assets/
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/enterprise-multilingual-service.git

cd enterprise-multilingual-service

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🚀 How It Works

1. Detect the input language.
2. Tokenize text using SentencePiece.
3. Translate using MarianMT.
4. Display translated text.
5. Convert translated text into speech using gTTS.
6. Allow users to download the generated audio.

---

## 🌐 Supported Languages

- English
- French
- German
- Spanish
- Italian
- Hindi

*(Extendable using additional MarianMT models.)*

---

## 🔮 Future Improvements

- Offline TTS using Coqui TTS
- Whisper speech recognition
- REST API
- Docker support
- Batch translation
- Translation memory
- User authentication
- Kubernetes deployment

---

## 📈 Resume Highlights

- Built a multilingual translation application using MarianMT and Hugging Face Transformers.
- Integrated automatic language detection and speech synthesis into an end-to-end NLP workflow.
- Managed model dependencies including SentencePiece and PyTorch for local inference.
- Developed an interactive Streamlit interface for translation and downloadable audio generation.

---

## 📄 License

MIT License