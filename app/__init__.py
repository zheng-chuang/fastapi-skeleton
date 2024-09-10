from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages.router, prefix="", tags=["pages"])

# ... 其他代码 ...
