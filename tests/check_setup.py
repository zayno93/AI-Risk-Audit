
import ollama

with open("system_prompt.txt", "r", encoding="utf-8") as file:
    system = file.read()

reply = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": "Hi, what can you help me with?"},
    ],
)

print(reply["message"]["content"])
