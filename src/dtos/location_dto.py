""" Module for CreateLocationDTO
"""

from dataclasses import dataclass, asdict

from src.domain.location import Location


@dataclass
class CreateLocationInputDto:
    """ Input Dto for create location """
    address: str
    city: str
    country: str

    def to_dict(self):
        """ Convert data into dictionary
        """
        return asdict(self)


@dataclass
class CreateLocationOutputDto:
    """ Output Dto for create location """
    location: Location
