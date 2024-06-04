from dataclasses import dataclass, asdict

from src.domain.people import People


@dataclass
class CreatePeopleInputDto:
    email: str
    password: str
    first_name: str
    last_name: str

    def to_dict(self):
        return asdict(self)


@dataclass
class CreatePeopleOutputDto:
    people: People
