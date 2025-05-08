from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat/")
async def chat(message: Message):
    # Here you would integrate with LiteLLM or another LLM service
    response = requests.post("https://api.example.com/llm", json={"input": message.user_input})
    return response.json()