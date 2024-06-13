from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers import deal
from app.utils.logging import AppLogger
import app.database as database

logger = AppLogger().get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the redis connection
    await database.init_db()
    try:
        yield
    finally:
        pass
        
app = FastAPI(title="Test", description="Test", version="0.0.1", lifespan=lifespan)


    
app.include_router(deal.router, tags=['Deal'], prefix="/api")