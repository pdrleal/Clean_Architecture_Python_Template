import abc


class IPeopleController(abc.ABC):

    @abc.abstractmethod
    def create(self):
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
