from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Body

from app import curd, models, schemas
from app.routers.deps import SessionDep

router = APIRouter(prefix="/api")


@router.post("/register", response_model=models.User)
async def register(db: SessionDep, user_create: Annotated[schemas.user.UserCreate, Body()]):
    user = curd.get_user_by_email(db=db, email=user_create.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    user = curd.create_user(db=db, user_create=user_create)
    return user
