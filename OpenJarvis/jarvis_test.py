import requests

response = requests.post(
    "http://127.0.0.1:8000/v1/chat/completions",
    json={
        "model": "llama3.2",
        "messages": [
            {
                "role": "user",
                "content": "สวัสดี"
            }
        ]
    }
)

print(response.json())
