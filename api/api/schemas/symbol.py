from pydantic import BaseModel


class Symbol(BaseModel):
    exchange: str
    symbol: str
    status: str
    base_asset: str
    base_asset_precision: int
    quote_asset: str
    quote_asset_precision: int
    quote_precision: int
    order_types: str

    class Config:
        orm_mode = True
