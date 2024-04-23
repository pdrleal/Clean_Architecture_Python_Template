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
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now())


load_dotenv(find_dotenv())
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
db_name = os.getenv('MYSQL_DB_NAME')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
# self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")
engine = create_engine('sqlite:///C:\\sqlitedbs\\test.db', echo=True)
session = sessionmaker(bind=engine)
session = scoped_session(session)
Base.metadata.create_all(engine)
