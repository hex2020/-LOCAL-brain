#!/bin/bash
echo "🧠 SETTING UP LOCAL BRAIN..."

# 1. Check for Ollama
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama not found! Launching installer..."
    # Unzip the included installer
    unzip -o installers/Ollama-darwin.zip
    # Run the app
    open Ollama.app
    echo "👉 Please follow the Ollama setup steps (Move to Applications), then run this script again!"
    exit 1
fi

# 2. Setup Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Download Models
ollama list | grep -q "llama3" || ollama pull llama3
ollama list | grep -q "nomic-embed-text" || ollama pull nomic-embed-text

# 4. Run
streamlit run app.py
