from sqlmodel import SQLModel, create_engine

from ..models.models import Customer

from .consts import DB_ECHO
from .config import get_db_settings

db_settings = get_db_settings()

db_url = db_settings.db_url
engine = create_engine(db_url, echo=DB_ECHO)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)