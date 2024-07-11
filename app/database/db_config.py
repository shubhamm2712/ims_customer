from sqlmodel import SQLModel, create_engine

from ..models.models import CustomerBroker, Customer, Broker

from ..config.consts import DB_FILE_NAME, DB_ECHO

sqlite_file_name = DB_FILE_NAME
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=DB_ECHO, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)