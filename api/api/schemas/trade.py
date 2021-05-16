from decimal import Decimal
from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel


class Trade(BaseModel):
    exchange: str
    symbol: str
    trade_id: int
    user_id: int
    order_id: int
    order_list_id: List[int]
    price: Decimal
    quantity: Decimal
    quote_quantity: Decimal
    commission: Decimal
    commission_asset: str
    traded_at: datetime
    is_buyer: bool
    is_maker: bool
    is_best_match: bool

    class Config:
        orm_mode = True
