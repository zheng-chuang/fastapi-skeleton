from fastapi import APIRouter, Request

from app.routers.deps import templates

router = APIRouter()


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
