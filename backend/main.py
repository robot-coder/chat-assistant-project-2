from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    user_input: str
    llm_choice: str

@app.post("/chat/")
async def chat(message: Message):
    # Here you would integrate with LiteLLM or another LLM service
    response = requests.post(f"https://api.example.com/llm/{message.llm_choice}", json={"input": message.user_input})
    return response.json()