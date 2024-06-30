from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from database.config import Config

Base = declarative_base()


def connection(isolation_level: str = "READ COMMITTED") -> Session:
    engine = create_engine(f"postgresql+asyncpg://{Config.user}:{Config.password}@{Config.host}:{Config.port}/{Config.name}", isolation_level=isolation_level)
    session = Session(bind=engine)
    return session


def async_connection(isolation_level: str = "READ COMMITTED"):
    engine = create_async_engine(f"postgresql+asyncpg://{Config.user}:{Config.password}@{Config.host}:{Config.port}/{Config.name}", isolation_level=isolation_level)
    session = sessionmaker(bind=engine, class_=AsyncSession)
    return session, engine
