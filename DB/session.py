from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import bot_settings


DB_URL = (
    f"postgresql+asyncpg://{bot_settings.DB_USER}:{bot_settings.DB_PASS}@"
    f"{bot_settings.DB_HOST}:{bot_settings.DB_PORT}/{bot_settings.DB_NAME}"
)


engine = create_async_engine(DB_URL)


async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
