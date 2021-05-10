from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        Numeric, String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import functions as func

from api.models.base import Base


class Trade(Base):
    __tablename__ = "trades"

    exchange = Column(String, primary_key=True, index=True)
    symbol = Column(String, primary_key=True, index=True)
    trade_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    order_list_id = Column(Integer)
    price = Column(Numeric)
    quantity = Column(Numeric)
    quote_quantity = Column(Numeric)
    commission = Column(Numeric)
    commission_asset = Column(String)
    traded_at = Column(DateTime, index=True)
    is_buyer = Column(Boolean, index=True)
    is_maker = Column(Boolean, index=True)
    is_best_match = Column(Boolean, index=True)
    created_at = Column(DateTime, index=True, server_default=func.now())
    updated_at = Column(DateTime, index=True, server_default=func.now(), onupdate=func.now())

    # owner_id = Column(Integer, ForeignKey('users.id'))
    # owner = relationship("User", back_populates="assets")
