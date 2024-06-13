
import asyncpg
import os
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from google.cloud.sql.connector import Connector, create_async_connector
from google.oauth2 import service_account
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.config import settings as global_settings
from app.utils.logging import AppLogger

logger = AppLogger().get_logger()

credentials_path = "secret_for_credentials.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

# Placeholder for session factory; will be set in `startup` event
AsyncSessionFactory = None

async def init_connection_pool(connector: Connector) -> AsyncEngine:
    # initialize Connector object for connections to Cloud SQL
    async def getconn() -> asyncpg.Connection:
        conn: asyncpg.Connection = await connector.connect_async(
           global_settings.instance_connection_name,
            "asyncpg",
            user=global_settings.db_user,
            password=global_settings.db_password,
            db=global_settings.db_name
        )
        return conn

    # The Cloud SQL Python Connector can be used along with SQLAlchemy using the
    # 'async_creator' argument to 'create_async_engine'
    pool = create_async_engine(
        "postgresql+asyncpg://",
        async_creator=getconn,
    )
    return pool

async def init_db():
    global AsyncSessionFactory
    
    connector = await create_async_connector(credentials=credentials)
    
    pool = await init_connection_pool(connector=connector)

    # Define the AsyncSession factory
    AsyncSessionFactory = async_sessionmaker(
        pool,
        autoflush=False,
        expire_on_commit=False,
    )
    

# Dependency: Get DB session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        yield session