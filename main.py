# backende kullanılan fonksiyonlar burada tanımlanmıştır.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

#izinler * yaptık güvenli değil biliyorum ama test için yaptım
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class Item(BaseModel):
    num1: int
    num2: int
    operation: str

@app.post("/calculate")
async def calculate(item: Item):
    if item.operation == "+":
        return item.num1 + item.num2
    elif item.operation == "-":
        return item.num1 - item.num2
    elif item.operation == "*":
        return item.num1 * item.num2
    elif item.operation == "/":
        return item.num1 / item.num2
    else:
        return "Unknown operation"

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

