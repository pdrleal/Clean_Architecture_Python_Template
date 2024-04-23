import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from src.domain.base.base_class import session


class DBContext:

    def __init__(self):
        load_dotenv(find_dotenv())
        user = os.getenv('MYSQL_USER')
        password = os.getenv('MYSQL_PASSWORD')
        db_name = os.getenv('MYSQL_DB_NAME')
        host = os.getenv('MYSQL_HOST')
        port = os.getenv('MYSQL_PORT')
        # self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")
        #self.engine = create_engine('sqlite:///C:\\sqlitedbs\\test.db', echo=True)
        #self.session = sessionmaker(bind=self.engine)
        #self.session = scoped_session(self.session)

