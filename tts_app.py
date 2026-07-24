import webbrowser
import os
from google import genai
import wave
import base64
import gradio as gr
import shutil

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

def tts(prompt, speaker, wavname, savedirectory, auto_open):
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
    file = wavname + ".wav"
    wave_file(file, base64.b64decode(interaction.output_audio.data))
    if not savedirectory:
        savedirectory = "wavs"
    shutil.move(file, savedirectory)
    fullpath = os.path.join(savedirectory, file)
    if auto_open:
        os.startfile(fullpath)
    return f"音声ファイルを保存しました: {fullpath}"

webbrowser.open('http://127.0.0.1:7860')

demo = gr.Interface(
    fn=tts,
    title="gemini-3.1-flash-tts-preview",
    description="wavnameについて：拡張子はいりません。　speakerについて：https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja&_gl=1*2p2973*_up*MQ..*_ga*NzAzNDQ1OC4xNzg0OTAxNDM1*_ga_P1DBVKWT6V*czE3ODQ5MDE0MzQkbzEkZzAkdDE3ODQ5MDE0MzQkajYwJGwwJGg0MDMyMjU1MTU.#voices",
    inputs=["text", "text", "text", "text", "checkbox"],
    outputs=["text"],
    api_name="gemini-3.1-flash-tts-preview",
)

demo.launch()