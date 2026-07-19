from google import genai

with open('.txt', "r", encoding="utf-8") as f:
    content = f.read()

client = genai.Client(api_key=content)

gemini_history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "{message}"}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=gemini_history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    gemini_history.append(step.model_dump())

gemini_history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=gemini_history
)
print("Response 2:", interaction2.steps[-1].content[0].text)