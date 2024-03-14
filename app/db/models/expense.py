from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    currency = Column(String)
    timestamp = Column(DateTime)

    category = relationship("Category", back_populates="expenses")
