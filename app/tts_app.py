import webbrowser
import os
from google import genai
import wave
import base64
import gradio as gr
import platform

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

def tts(prompt, speaker, save_directory, file_name, auto_open):
    if not prompt:
        return "プロンプトを入力してください(エラー400を防ぎました)。"
    interaction = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=prompt,
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": speaker if speaker else "Kore"}
            ]
        }
    )

    if not save_directory:
        if platform.system() == "Windows":
            import getpass
            save_directory = f"C:/Users/{getpass.getuser()}/Music/"
        else:
            return "保存ディレクトリを入力してください。"

    if not file_name:
        file_name = "output.wav"
    else:
        file_name += ".wav"

    save_path = os.path.join(save_directory, file_name)

    wave_file(save_path, base64.b64decode(interaction.output_audio.data))

    if auto_open:
        if platform.system() == "Windows":
            os.startfile(save_path)
        elif platform.system() == "Linux":
            from playsound import playsound
            playsound(save_path)

    return f"音声ファイルを保存しました: {save_path}"

webbrowser.open('http://127.0.0.1:7860')

gr.Interface(
    fn=tts,
    title="gemini-3.1-flash-tts-preview",
    description="エラーはバックエンドウィンドウに表示されます。バックエンドウィンドウでctrl+Cを押すと終了します。prompt:入力テキスト。必ず入力してください。save_directory(デフォルトはC:/Users/{getpass.getuser()}/Music/)：音声を保存するディレクトリ。　file_name(デフォルトはoutput.wav)：保存するファイル名。拡張子はいりません。　speaker(デフォルトはKore)：話者。種類https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja&_gl=1*2p2973*_up*MQ..*_ga*NzAzNDQ1OC4xNzg0OTAxNDM1*_ga_P1DBVKWT6V*czE3ODQ5MDE0MzQkbzEkZzAkdDE3ODQ5MDE0MzQkajYwJGwwJGg0MDMyMjU1MTU.#voices",
    inputs=["text", "text", "text", "text", "checkbox"],
    outputs=["text"],
    examples=[["こんにちは", "", "", "", True]],
    api_name="gemini-3.1-flash-tts-preview",
).launch()
