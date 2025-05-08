from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    user_input: str
    llm_choice: str

conversation_history = []

@app.post("/chat/")
async def chat(message: Message):
    # Store the user input in the conversation history
    conversation_history.append({"role": "user", "content": message.user_input})
    # Here you would integrate with LiteLLM or another LLM service
    response = requests.post(f"https://api.example.com/llm/{message.llm_choice}", json={"input": message.user_input})
    assistant_response = response.json().get('response')
    # Store the assistant's response in the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_response})
    return {
        "response": assistant_response,
        "conversation_history": conversation_history
    }