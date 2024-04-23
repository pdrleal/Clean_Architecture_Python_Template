import abc

from src.domain.event import Event


class IEventRepo(abc.ABC):
    @abc.abstractmethod
    def add(self, event_model: Event):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def deactivate(self):
        pass
