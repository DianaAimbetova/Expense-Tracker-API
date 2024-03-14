from pydantic import BaseModel
from typing import Optional


class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ExpenseUpdate(BaseModel):
    name: Optional[str]


class ExpenseCreate(BaseModel):
    name: Optional[str]
