import requests

def fetch_emails():
    res = requests.get("http://localhost:8025/api/v2/messages")
    messages = res.json().get("items", [])
    return messages
