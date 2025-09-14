#!/bin/bash

echo "🔧 Updating system packages..."
sudo apt-get update && sudo apt-get upgrade -y

echo "📦 Installing system-level dependencies..."
sudo apt-get install -y \
    build-essential \
    ffmpeg \
    libsndfile1 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    python3-dev \
    python3-pip \
    git \
    curl \
    wget

echo "🧠 Installing Python packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🗣️ Downloading NLTK and spaCy models..."
python3 -m nltk.downloader punkt wordnet stopwords
python3 -m spacy download en_core_web_sm
