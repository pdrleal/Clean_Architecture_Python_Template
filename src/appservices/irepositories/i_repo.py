import abc


class IRepo(abc.ABC):
    @abc.abstractmethod
    def add(self, model):
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
