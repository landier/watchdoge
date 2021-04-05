from sqlalchemy import (BigInteger, Column, DateTime, Float, Integer,
                        Numeric, String)
from sqlalchemy.sql import functions as func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.models.base import Base


class Ticker(Base):
    __tablename__ = "tickers"

    id = Column(Integer, primary_key=True, index=True)
    exchange = Column(String, index=True)
    symbol = Column(String, index=True)
    price_change = Column(Numeric, index=True)
    price_change_percent = Column(Float, index=True)
    weighted_avg_price = Column(Numeric, index=True)
    prev_close_price = Column(Numeric)
    last_price = Column(Numeric, index=True)
    last_qty = Column(Float, index=True)
    bid_price = Column(Numeric)
    bid_qty = Column(Float)
    ask_price = Column(Numeric)
    ask_qty = Column(Float)
    open_price = Column(Numeric, index=True)
    high_price = Column(Numeric, index=True)
    low_price = Column(Numeric, index=True)
    volume = Column(Numeric, index=True)
    quoteVolume = Column(Numeric, index=True)
    open_time = Column(DateTime)
    close_time = Column(TIMESTAMP)
    first_id = Column(BigInteger)
    last_id = Column(BigInteger)
    count = Column(Integer, index=True)
    created = Column(DateTime, index=True, server_default=func.now())

"""
    "symbol": "ETHBTC",
    "priceChange": "-0.00015700",
    "priceChangePercent": "-0.439",
    "weightedAvgPrice": "0.03546381",
    "prevClosePrice": "0.03572700",
    "lastPrice": "0.03557500",
    "lastQty": "0.73500000",
    "bidPrice": "0.03557500",
    "bidQty": "3.17100000",
    "askPrice": "0.03557700",
    "askQty": "29.83300000",
    "openPrice": "0.03573200",
    "highPrice": "0.03596100",
    "lowPrice": "0.03491900",
    "volume": "208332.96900000",
    "quoteVolume": "7388.28016430",
    "openTime": 1617480029055,
    "closeTime": 1617566429055,
    "firstId": 247666147,
    "lastId": 247922366,
    "count": 256220
"""
