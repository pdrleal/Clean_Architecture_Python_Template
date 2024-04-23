import json
import os

import pandas as pd
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, text

from src.appservices.irepositories.ievent_repo import IEventRepo
from src.domain.base.base_class import Base
from src.infrastructure.persistence.dbcontext import DBContext
from src.domain.base.base_class import session

class EventRepo(IEventRepo):

    def __init__(self, db_context: DBContext):
        self.db_context = DBContext()

    def add(self, event_model):
        session.add(event_model)
        session.commit()

    def get(self):
        pass

    def update(self):
        pass

    def deactivate(self):
        pass
