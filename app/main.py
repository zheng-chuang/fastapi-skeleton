from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import api_router, pages_router

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
app.include_router(pages_router)
