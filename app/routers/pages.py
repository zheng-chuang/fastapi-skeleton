from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from pathlib import Path
from sqlmodel import Session, select
from app.database import get_session
from app.models.singer import Singer

router = APIRouter()

directory = str(Path(__file__).parent.parent.parent / "templates")

print(directory)

templates = Jinja2Templates(directory=directory)


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


