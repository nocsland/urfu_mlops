import requests

url = "http://91.185.85.43:8000/translate/en-to-ru/"
payload = {"text": "The quick brown fox jumps over the lazy dog."}
response = requests.post(url, json=payload)
print(response.json())
