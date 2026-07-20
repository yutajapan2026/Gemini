import webbrowser
import gradio as gr
from google import genai

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

print("履歴を作成しています...")

interaction = client.interactions.create(
model="gemini-3.5-flash",
input="",
)

webbrowser.open('http://127.0.0.1:7860')

def gemini(message, history):
    global interaction
    interaction = client.interactions.create(
    model="gemini-3.5-flash",
    previous_interaction_id=interaction.id,
    input=message,
    )
    return interaction.output_text

gr.ChatInterface(
    fn=gemini,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Geminiに相談", container=False, scale=7),
    title="Gemini",
    description="何かお手伝いできることはありますか？エラーはバックエンドウィンドウに表示されます。バックエンドウィンドウを閉じると終了します。※プライバシーについての公式見解: https://support.google.com/gemini?p=privacy_help",
    examples=["こんにちは", "Geminiとは何ですか?", "Pythonとは何ですか?"],
    cache_examples=True,
).launch()