from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    item: str
    amount: float
    tax_rate: float

@app.post("/calculate-total")
async def calculate_total(order: Order):
    
    total = round(order.amount + (order.amount * (order.tax_rate / 100)), 2)

    return {"item": order.item, "total": total}