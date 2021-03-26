from decimal import Decimal
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
import sqlalchemy

from api.models.base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")




# from api.database import SessionLocal

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# wallet = Wallet(exchange='Binance', symbol='USD', balance=Decimal(4), free=Decimal(3), locked=Decimal(1))
# db = SessionLocal()
# db.add(wallet)
# db.commit()
