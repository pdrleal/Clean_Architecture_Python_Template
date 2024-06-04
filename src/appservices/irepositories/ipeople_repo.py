import abc

from src.domain.people import People


class IPeopleRepo(abc.ABC):
    @abc.abstractmethod
    def add(self, model: People):
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
