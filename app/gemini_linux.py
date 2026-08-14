import webbrowser
import os
import tkinter as tk

def api_key_input():
    root = tk.Tk()
    root.title("Gemini - APIキーの入力")
    root.state("normal")
    label1 = tk.Label(root, text="Gemini", font=("Arial", 30))
    label1.pack()
    label3 = tk.Label(root, text="APIキーを入力してください", fg="blue", cursor="hand2", font=("Arial", 10), underline=True)
    label3.pack(pady=(0, 10))
    entry = tk.Entry(root, show="*", width=30)
    entry.pack()
    def close():
        with open('.txt', 'w') as file:
            file.write(entry.get())
        root.destroy()
    button = tk.Button(root, text="送信", command=close)
    button.pack()
    root.mainloop()

if os.path.exists('.txt'):
    pass
else:
    api_key_input()

root = tk.Tk()
root.title("Gemini - ホーム")
root.state("normal")
label1 = tk.Label(root, text="Gemini", font=("Arial", 30))
label1.pack()
img = tk.PhotoImage(file="logo.png")
label2 = tk.Label(root, image=img, font=("Arial", 30))
label2.pack()
def gemini_chat():
    import chat_app

button1 = tk.Button(root, text="チャット", command=gemini_chat)
button1.pack()
def gemini_tts():
    import tts_app

button2 = tk.Button(root, text="音声合成", command=gemini_tts)
button2.pack()
button3 = tk.Button(root, text="APIキーの修正", command=api_key_input)
button3.pack()
root.mainloop()
