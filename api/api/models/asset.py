from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String, Numeric)
from sqlalchemy.sql import functions as func

from api.models.base import Base


class Asset(Base):
    __tablename__ = "assets"

    exchange = Column(String, primary_key=True, index=True)
    asset = Column(String, primary_key=True, index=True)
    withdraw_fee = Column(Numeric)
    min_withdraw_amount = Column(Numeric)
    withdraw_status = Column(Boolean)
    deposit_status = Column(Boolean)
    created_at = Column(DateTime, index=True, server_default=func.now())
    updated_at = Column(DateTime, index=True, server_default=func.now(), onupdate=func.now())
