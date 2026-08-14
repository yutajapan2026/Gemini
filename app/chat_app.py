import webbrowser
import gradio as gr
from google import genai
import platform

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

print("履歴を作成しています...")

interaction = client.interactions.create(
model="gemini-3.6-flash",
input="hello",
generation_config={
        "thinking_level": "low"
    }
)

def gemini(message, history):
    global interaction
    if not message:
        return "プロンプトを入力してください(エラー400を防ぎました)。"
    interaction = client.interactions.create(
    model="gemini-3.6-flash",
    previous_interaction_id=interaction.id,
    input=message,
    generation_config={
        "thinking_level": "low"
    }
    )
    return interaction.output_text

if platform.system() == "Windows":
    webbrowser.open('http://127.0.0.1:7860')

gr.ChatInterface(
    fn=gemini,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Geminiに相談", container=False, scale=7),
    title="gemini-3.6-flash",
    description="何かお手伝いできることはありますか？※エラーはバックエンドウィンドウに表示されます。※バックエンドウィンドウでctrl+Cを押すと終了します。※プライバシーについての公式見解: https://support.google.com/gemini?p=privacy_help",
    examples=["こんにちは", "Geminiとは何ですか?", "Pythonとは何ですか?"],
    cache_examples=True,
).launch()