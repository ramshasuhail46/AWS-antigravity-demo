from decimal import Decimal, ROUND_HALF_UP
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    item: str
    amount: Decimal
    tax_rate: Decimal

@app.post("/calculate-total")
async def calculate_total(order: Order):
    
    total = order.amount + (order.amount * (order.tax_rate / Decimal('100')))
    
    # Round to 2 decimal places for currency
    rounded_total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return {"item": order.item, "total": float(rounded_total)}