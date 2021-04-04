from decimal import Decimal

from pydantic import BaseModel


class Asset(BaseModel):
    exchange: str
    symbol: str
    balance: Decimal
    free: Decimal
    locked: Decimal
    class Config:
        orm_mode = True
