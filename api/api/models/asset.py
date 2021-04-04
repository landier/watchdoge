from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from api.models.base import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    exchange = Column(String, index=True)
    symbol = Column(String, index=True)
    balance = Column(Numeric, index=True)
    free = Column(Numeric, index=True)
    locked = Column(Numeric, index=True)

    # owner_id = Column(Integer, ForeignKey('users.id'))
    # owner = relationship("User", back_populates="assets")
