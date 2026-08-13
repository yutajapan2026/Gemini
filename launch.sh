#!/usr/bin/env bash

${VENV_DIR:="venv"}

sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip

echo "仮想環境を作成中..."
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

echo "pip を更新中..."
python -m pip install --upgrade pip

echo "google-genai と gradio をインストール中..."
python -m pip install google-genai gradio

echo "アプリを起動中..."
cd app
python gemini.py
