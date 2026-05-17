@echo off
title Gemini - 起動しています...
python --version
if not %errorlevel% == 0 (
    title Gemini - Pythonがインストールされていません
    curl  -L -O "https://www.python.org/ftp/python/3.14.4/python-3.14.4-amd64.exe"
    echo msgbox "Pythonインストーラを開きます。「Add python.exe to PATH」へチェックを入れ、「Install Now」を選択してください。インストールできたらこのアプリをもう一度起動してください。" > %TEMP%/msgboxtest.vbs & %TEMP%/msgboxtest.vbs
    start python-3.14.4-amd64.exe & exit
)

if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install gradio google-genai
title Gemini - ようこそ
python gemini.py