import os
import asyncio
from alembic import context
import sqlalchemy
from google.cloud.sql.connector import Connector
from google.oauth2 import service_account
from app.config import settings as global_settings
from app.utils.logging import AppLogger
from app.models.base import Base

logger = AppLogger().get_logger()

credentials_path = os.path.join("secret_for_credentials.json")

credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

target_metadata = Base.metadata
# target_metadata = None

def do_run_migrations(connection):
    context.configure(
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True,
        # literal_binds=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # logger.info(settings.asyncpg_url.unicode_string())
    connector = Connector(credentials=credentials)

    def getconn():
        conn = connector.connect(
            global_settings.instance_connection_name,
            "pg8000",
            user=global_settings.db_user,
            password=global_settings.db_password,
            db=global_settings.db_name
        )
        return conn
    
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    # connectable = create_async_engine(settings.asyncpg_url.unicode_string(), future=True)

    with pool.connect() as connection:
        # pass
        do_run_migrations(connection)
        # connection.run_sync(do_run_migrations)

    pool.dispose()  # Ensure the engine is disposed
    connector.close()  # Ensure the connector is closed

asyncio.run(run_migrations_online())