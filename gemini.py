import os
import tkinter as tk

if os.path.exists('.txt'):
    pass
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

root = tk.Tk()
root.title("Gemini")
root.state("zoomed")
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
root.mainloop()
