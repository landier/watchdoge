from decimal import Decimal

from pydantic import BaseModel


class Asset(BaseModel):
    exchange: str
    asset: str
    withdraw_fee: Decimal
    min_withdraw_amount: Decimal
    deposit_status: bool
    withdraw_status: bool

    class Config:
        orm_mode = True
