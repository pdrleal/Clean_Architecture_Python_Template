from src.appservices.irepositories.ievent_repo import IEventRepo
from src.appservices.iservices.ievent_service import IEventService
from src.domain.event import Event
from src.domain.location import Location
from src.dtos.event_dto import CreateEventInputDto


class EventService(IEventService):

    def __init__(self, event_repo: IEventRepo):
        self.event_repo = event_repo

    def create(self, event_dto: CreateEventInputDto):
        event_model = Event(name=event_dto.name, recurring=event_dto.recurring, event_type=event_dto.event_type,
                            start_datetime=event_dto.start_datetime, end_datetime=event_dto.end_datetime,
                            location=Location(
                                address=event_dto.location.address, city=event_dto.location.city,
                                country=event_dto.location.country))
        self.event_repo.add(event_model)
        pass

    def get_all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
