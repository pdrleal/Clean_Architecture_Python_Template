import abc

from src.dtos.event_dto import CreateEventInputDto


class IEventService(abc.ABC):

    @abc.abstractmethod
    def create(self, event_dto: CreateEventInputDto):
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
