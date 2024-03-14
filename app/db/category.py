from sqlalchemy.orm import Session
from api.models.category import CategoryUpdate, CategoryCreate, Category


def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: int):
    return db.query(Category)\
        .filter(Category.id == category_id)\
        .first()


def update_category(db: Session, category_id: int,
                    category_update: CategoryUpdate):
    db_category = db.query(Category)\
        .filter(Category.id == category_id)\
        .first()
    if db_category:
        for field, value in category_update.dict(exclude_unset=True).items():
            setattr(db_category, field, value)
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(Category)\
        .filter(Category.id == category_id)\
        .first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category
