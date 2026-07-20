import os
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input=input("音声合成したい文章を入力してください: "),
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))

os.startfile("out.wav")