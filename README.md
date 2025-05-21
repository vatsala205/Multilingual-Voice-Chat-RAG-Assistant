# Multilingual-Voice-Chat-RAG-Assistant
# 🎙️ Multilingual Voice Chat RAG Assistant

A prototype AI system for visually impaired users that supports **multilingual voice input** and uses **Retrieval-Augmented Generation (RAG)** to help users interact with accessible content.

This project was developed as part of the **Flickdone AI Platform Developer Assessment**.

---

## 🔧 Features

- 🗣️ **Speech-to-Text (STT)** using OpenAI Whisper  
- 📚 **Semantic Document Retrieval** using FAISS + Sentence Transformers  
- 🤖 **Natural Language Generation** using OpenAI GPT  
- 🌍 **Multilingual Support** (e.g., English, Hindi, etc.)  
- 🔁 Modular, on-premise-ready architecture  
- 🛠️ Text output (TTS in progress)

---

## 📁 Folder Structure

multilingual-rag/
├── audio_inputs/ # Input .wav audio files
├── corpus/ # Text documents for retrieval
├── modules/ # Modular Python files
│ ├── stt_module.py # Speech-to-text (Whisper)
│ ├── embedding_module.py # Embedding + retrieval (FAISS)
│ └── generation_module.py# GPT-based answer generation
├── outputs/ # (To be used for TTS output)
├── main.py # Main pipeline script
└── requirements.txt # Required Python packages
