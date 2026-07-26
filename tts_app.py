import webbrowser
import os
from google import genai
import wave
import base64
import gradio as gr
import getpass
from tkinter import filedialog

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

def tts(prompt, speaker, custom_save, auto_open):
    interaction = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=prompt,
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": speaker}
            ]
        }
    )
    
    if custom_save:
        save_path = filedialog.asksaveasfilename(
            title="名前を付けて保存",
            initialdir=f"C:/Users/{getpass.getuser()}/Music",
            defaultextension=".wav",
            filetypes=[("Waveファイル", "*.wav"), ("すべてのファイル", "*.*")]
        )
    else:
        save_path = f"C:/Users/{getpass.getuser()}/Music/output.wav"

    wave_file(save_path, base64.b64decode(interaction.output_audio.data))

    if auto_open:
        os.startfile(save_path)
    
    return f"音声ファイルを保存しました: {save_path}"

webbrowser.open('http://127.0.0.1:7860')

gr.Interface(
    fn=tts,
    title="gemini-3.1-flash-tts-preview",
    description="speakerについて(デフォルトはKore)：https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja&_gl=1*2p2973*_up*MQ..*_ga*NzAzNDQ1OC4xNzg0OTAxNDM1*_ga_P1DBVKWT6V*czE3ODQ5MDE0MzQkbzEkZzAkdDE3ODQ5MDE0MzQkajYwJGwwJGg0MDMyMjU1MTU.#voices",
    inputs=["text", "text", "checkbox", "checkbox"],
    outputs=["text"],
    api_name="gemini-3.1-flash-tts-preview",
).launch()
