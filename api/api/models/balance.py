from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        Numeric, String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import functions as func

# from sqlalchemy.sql.sqltypes import Date, DateTime
from api.models.base import Base


class Balance(Base):
    __tablename__ = "balances"

    # id = Column(Integer, primary_key=True, index=True)
    exchange = Column(String, primary_key=True, index=True)
    asset = Column(String, primary_key=True, index=True)
    balance = Column(Numeric, index=True)
    free = Column(Numeric, index=True)
    locked = Column(Numeric, index=True)
    created_at = Column(DateTime, index=True, server_default=func.now())
    updated_at = Column(DateTime, index=True, server_default=func.now(), onupdate=func.now())

    # owner_id = Column(Integer, ForeignKey('users.id'))
    # owner = relationship("User", back_populates="assets")
