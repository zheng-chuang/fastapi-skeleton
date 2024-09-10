from sqlmodel import Session, select
from app import models, schemas
from app.utils.auth import get_password_hash


def get_user_by_email(*, db: Session, email: str):
    query = select(models.User).where(models.User.email == email)
    db_user = db.exec(query).first()
    if db_user:
        return db_user
    return None


def create_user(*, db: Session, user_create: schemas.user.UserCreate):
    user = models.User.model_validate(
        user_create,
        update={
            "hashed_password": get_password_hash(user_create.password)
        }
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
