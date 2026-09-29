from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "BankSaathi Backend is Running"}

@app.get("/bank-info")
def get_bank_info():
    return {"message": "Bank Information"}

@app.post("/ask")
def ask_question(data: Question):
    return {"question": data.question}