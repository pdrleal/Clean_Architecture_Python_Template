import os
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import func, create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, sessionmaker, scoped_session


class Base(DeclarativeBase):
    """define a series of common elements that may be applied to mapped
    classes using this class as a base class."""

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now(), nullable=True)
