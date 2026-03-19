from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Basic Login API")

class LoginRequest(BaseModel):
    username: str
    password: str

FAKE_USER = {
    "username": "admin",
    "password": "123456"
}

@app.get("/")
def root():
    return {"message": "Python Login API is running"}

@app.post("/login")
def login(payload: LoginRequest):
    if payload.username == FAKE_USER["username"] and payload.password == FAKE_USER["password"]:
        return {
            "success": True,
            "message": "Login successful",
            "token": "demo-token-123"
        }
    raise HTTPException(status_code=401, detail="Invalid username or password")
