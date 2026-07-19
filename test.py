from google import genai

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

chat = client.chats.create(model='gemini-3.5-flash')
response = chat.send_message('tell me a story')
print(response.text)
response = chat.send_message('summarize the story you told me in 1 sentence')
print(response.text)