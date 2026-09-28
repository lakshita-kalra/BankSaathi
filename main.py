from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "BankSaathi Backend is Running"}
@app.get("/bank-info")
def get_bank_info():
    return {"message": "Bank Information"}