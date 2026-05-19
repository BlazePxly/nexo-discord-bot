import os
from openai import OpenAI

SUMOPOD_API_KEY = "sk-1PKKu1j1cT2zGCsk0eEn4Q"

client = OpenAI(
    api_key=SUMOPOD_API_KEY,
    base_url="https://api.sumopod.com/v1"
)

print("Available models on Sumopod:")
try:
    models = client.models.list()
    for m in models:
        print(m.id)
except Exception as e:
    print(f"Failed to list models: {e}")
