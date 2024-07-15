from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from .config.config import get_settings

from .database.db_config import create_db_and_tables

from .routes import customers, brokers

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan = lifespan)

settings = get_settings()
origins = ["*"] if settings.origin is None else settings.origin.split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customers.apiRouter)
app.include_router(brokers.apiRouter)