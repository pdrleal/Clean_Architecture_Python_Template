""" Module for CreateEvent Dto
    DTO is a data transfer object, it is used to pass data between the layers of the application.
"""

from dataclasses import dataclass, asdict
from datetime import datetime

from src.domain.event import Event
from src.domain.location import Location
from src.dtos.location_dto import CreateLocationInputDto


@dataclass
class CreateEventInputDto:
    """ Input Dto for create event """
    name: str
    recurring: str
    event_type: str
    start_datetime: str
    end_datetime: str
    location: CreateLocationInputDto

    def to_dict(self):
        """ Convert data into dictionary
        """
        return asdict(self)

    def to_model(self):
        location_model = Location(address=self.location.address, city=self.location.city, country=self.location.country)
        event_model = Event(name=self.name,
                            recurring=self.recurring,
                            event_type=self.event_type,
                            start_datetime=datetime.strptime(self.start_datetime, "%Y-%m-%d %H:%M:%S"),
                            end_datetime=datetime.strptime(self.end_datetime, "%Y-%m-%d %H:%M:%S"),
                            location=location_model)
        return event_model


@dataclass
class CreateEventOutputDto:
    """ Output Dto for create event """
    event: Event
