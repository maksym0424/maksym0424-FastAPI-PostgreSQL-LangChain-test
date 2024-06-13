import os

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    instance_connection_name: str = os.getenv("INSTANCE_CONNECTION_NAME")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv("DB_NAME")
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    taviliy_api_key: str = os.getenv("TAVILY_API_KEY")

settings = Settings()
