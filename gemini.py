import webbrowser
import os
import tkinter as tk
import gradio as gr
from google import genai
import time

if os.path.exists('.txt'):
    root = tk.Tk()
    root.title("Gemini - APIキーの読み込みに成功しました")
    root.state("zoomed")
    label1 = tk.Label(root, text="Gemini", font=("Arial", 30))
    label1.pack()
    img = tk.PhotoImage(file="logo.png")
    label2 = tk.Label(root, image=img, font=("Arial", 30))
    label2.pack()
    def close():
        root.destroy()
    root.after(3000, close)
    root.mainloop()
else:
    root = tk.Tk()
    root.title("Gemini - APIキーの入力")
    root.state("zoomed")
    def link_click(url):
        webbrowser.open_new(url)
    label1 = tk.Label(root, text="Gemini", font=("Arial", 30))
    label1.pack()
    img = tk.PhotoImage(file="logo.png")
    label2 = tk.Label(root, image=img, font=("Arial", 30))
    label2.pack()
    label3 = tk.Label(root, text="APIキーをここから取得して入力してください", fg="blue", cursor="hand2", font=("Arial", 10), underline=True)
    label3.pack(pady=(0, 10))
    label3.bind("<Button-1>",lambda e:link_click("https://aistudio.google.com/api-keys"))
    entry = tk.Entry(root, show="*", width=30)
    entry.pack()
    def close():
        with open('.txt', 'w') as file:
            file.write(entry.get())
        root.destroy()
    button = tk.Button(root, text="送信", command=close)
    button.pack()
    root.mainloop()
    

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

webbrowser.open('http://127.0.0.1:7860')

def gemini(message, history):
    for attempt in range(5):
        try:
            interaction = client.interactions.create(
            model="gemini-3.5-flash",
            input=message
            )
            return interaction.output_text
        except errors.APIError as e:
            if e.code == 503:
                # 指数バックオフ: 2秒, 4秒, 8秒, 16秒, 32秒 + ランダムなジッター
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"503 High Demand - {attempt+1}回目のリトライ、{wait_time:.1f}秒待機中...")
                time.sleep(wait_time)
            elif e.code == 429:
                 # 429 レート制限：より長く待機
                wait_time = 60 + random.uniform(0, 10)
                print(f"429 Rate Limit - {attempt+1}回目のリトライ、{wait_time:.1f}秒待機中...")
                time.sleep(wait_time)
            else:
                raise  # その他のエラーは直接スロー
        raise Exception(f"{attempt}回のリトライ後も失敗しました")


gr.ChatInterface(
    fn=gemini,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Geminiに相談", container=False, scale=7),
    title="Gemini",
    description="何かお手伝いできることはありますか？※バックエンドウィンドウを閉じると終了します。※プライバシーについての公式見解: https://support.google.com/gemini?p=privacy_help",
    examples=["こんにちは", "Geminiとは何ですか?", "Pythonとは何ですか?"],
    cache_examples=True,
).launch()