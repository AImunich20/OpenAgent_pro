import json
import requests

url = "http://127.0.0.1:8000/v1/chat/completions"

payload = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": "2+3*4 เท่ากับเท่าไร"
        }
    ]
}

response = requests.post(url, json=payload)

data = response.json()

content = data["choices"][0]["message"]["content"]

print("AI RESPONSE:")
print(content)

# ถ้า AI เรียก tool
try:
    tool_call = json.loads(content)

    if tool_call["name"] == "calculate":
        expression = tool_call["parameters"]["expression"]

        result = eval(expression)

        print("\nTOOL RESULT:")
        print(result)

except:
    pass
