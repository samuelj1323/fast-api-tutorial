import uuid
from collections.abc import AsyncGenerator

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, relationship

DATABASE_URL = "sqlite+aiosqlite///./test.db"
