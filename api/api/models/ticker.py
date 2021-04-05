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
    price_change = Column(Numeric)
    price_change_percent = Column(Float, index=True)
    weighted_avg_price = Column(Numeric)
    prev_close_price = Column(Numeric)
    last_price = Column(Numeric, index=True)
    last_qty = Column(Float, index=True)
    bid_price = Column(Numeric)
    bid_qty = Column(Float)
    ask_price = Column(Numeric)
    ask_qty = Column(Float)
    open_price = Column(Numeric)
    high_price = Column(Numeric)
    low_price = Column(Numeric)
    volume = Column(Numeric)
    open_time = Column(String)
    close_time = Column(String)
    first_id = Column(BigInteger)
    last_id = Column(BigInteger)
    count = Column(Integer, index=True)
    created = Column(DateTime, index=True, server_default=func.now())

"""
    'askPrice': '1.19333000',
    'askQty': '221.20000000',
    'bidPrice': '1.19332000',
    'bidQty': '106.00000000',
    'closeTime': 1617652783169,
    'count': 506715,
    'firstId': 116705016,
    'highPrice': '1.21687000',
    'lastId': 117211730,
    'lastPrice': '1.19333000',
    'lastQty': '69.00000000',
    'lowPrice': '1.16222000',
    'openPrice': '1.18038000',
    'openTime': 1617566383169,
    'prevClosePrice': '1.18046000',
    'priceChange': '0.01295000',
    'priceChangePercent': '1.097',
    'quoteVolume': '349872702.60832400',
    'symbol': 'ADAUSDT',
    'volume': '294577254.70000000',
    'weightedAvgPrice': '1.18771119'}
"""
