import abc


class IEventController(abc.ABC):

    @abc.abstractmethod
    def create_event(self, input_json: dict):
        pass

    @abc.abstractmethod
    def get_events(self):
        pass

    @abc.abstractmethod
    def update_event(self):
        pass

    @abc.abstractmethod
    def delete_event(self):
        pass
