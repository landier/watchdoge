from typing import Optional
import os

from binance.client import Client

from fastapi import APIRouter
from pydantic import BaseModel


class Trade(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


router = APIRouter()

client = Client(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET')

@router.get("/wallet/")
async def get_wallet():
    balance = client.get_asset_balance(asset='BTC')
    return 1


@router.post("/items/")
async def create_item(item: Trade):
    return item
