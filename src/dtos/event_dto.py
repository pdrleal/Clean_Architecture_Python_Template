""" Module for CreateEvent Dto
    DTO is a data transfer object, it is used to pass data between the layers of the application.
"""

from dataclasses import dataclass, asdict

from src.domain.event import Event
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


@dataclass
class CreateEventOutputDto:
    """ Output Dto for create event """
    event: Event
