import abc

from src.dtos.people_dto import CreatePeopleInputDto


class IPeopleService(abc.ABC):

    @abc.abstractmethod
    def create(self, dto: CreatePeopleInputDto):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def delete(self):
        pass
