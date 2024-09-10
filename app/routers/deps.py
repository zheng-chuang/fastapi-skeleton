from typing import Annotated
from sqlmodel import Session

from app.database import get_session

SessionDep = Annotated[Session, get_session]
