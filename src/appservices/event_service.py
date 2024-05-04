from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.domain.base.base_class import Base

from src.appservices.irepositories.ievent_repo import IEventRepo
from src.appservices.iservices.ievent_service import IEventService
from src.domain.event import Event
from src.domain.location import Location
from src.dtos.event_dto import CreateEventInputDto


class EventService(IEventService):

    def __init__(self, event_repo: IEventRepo):
        self.event_repo = event_repo

    def create(self, event_dto: CreateEventInputDto):
        event_model = event_dto.to_model()

        engine = create_engine('sqlite:///C:\\sqlitedbs\\test.db', echo=True)
        session = sessionmaker(bind=engine)
        session = scoped_session(session)
        Base.metadata.create_all(engine)
        self.event_repo.add(event_model)
        pass

    def get_all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
