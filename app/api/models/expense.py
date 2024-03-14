from pydantic import BaseModel
from category import Category
from enum import Enum
from datetime import datetime
from typing import Optional


class Currency(str, Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'


class Expense(BaseModel):
    id: int
    category: Category
    amount: float
    description: str
    currency: Currency
    timestamp: datetime

    class Config:
        orm_mode = True


class ExpenseUpdate(BaseModel):
    amount: Optional[float]
    description: Optional[str]
    category_id: Optional[int]
    currency: Optional[str]
    timestamp: Optional[datetime]


class ExpenseCreate(BaseModel):
    amount: float
    description: str
    category_id: int
    currency: str
    timestamp: datetime
