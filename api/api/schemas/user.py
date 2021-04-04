from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from api.schemas.item import Item

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
