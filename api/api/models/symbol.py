from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.sql import functions as func

# from sqlalchemy.sql.sqltypes import Date, DateTime
from api.models.base import Base


class Symbol(Base):
    __tablename__ = "symbols"

    exchange = Column(String, primary_key=True, index=True)
    symbol = Column(String, primary_key=True, index=True)
    status = Column(String, index=True)
    base_asset = Column(String, index=True)
    base_asset_precision = Column(Integer)
    quote_asset = Column(String, index=True)
    quote_asset_precision = Column(Integer)
    quote_precision = Column(Integer)
    order_types = Column(String)
    created_at = Column(DateTime, index=True, server_default=func.now())
    updated_at = Column(DateTime, index=True, server_default=func.now(), onupdate=func.now())
