from typing import Annotated

from fastapi.params import Depends
from sqlmodel import Session
from fastapi.templating import Jinja2Templates

from app.config import settings

from app.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

templates = Jinja2Templates(directory=settings.TEMPLATES_PATH)
