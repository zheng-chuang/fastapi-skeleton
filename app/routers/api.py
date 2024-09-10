from fastapi import APIRouter

from app.routers.deps import SessionDep

router = APIRouter()


@router.get("/")
async def root(session: SessionDep):
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
