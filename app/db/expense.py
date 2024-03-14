from sqlalchemy.orm import Session
from api.models.expense import ExpenseUpdate, ExpenseCreate, Expense


def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def get_expense(db: Session, expense_id: int):
    return (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )


def update_expense(db: Session, expense_id: int,
                   expense_update: ExpenseUpdate):
    db_expense = db.query(Expense)\
        .filter(Expense.id == expense_id)\
        .first()
    if db_expense:
        for field, value in expense_update.dict(exclude_unset=True).items():
            setattr(db_expense, field, value)
        db.commit()
        db.refresh(db_expense)
    return db_expense


def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(Expense)\
        .filter(Expense.id == expense_id)\
        .first()
    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense
