from src.appservices.irepositories.ievent_repo import IEventRepo
from src.domain.base.base_class import session
from src.infrastructure.persistence.dbcontext import DBContext


class EventRepo(IEventRepo):

    def __init__(self, db_context: DBContext):
        self.db_context = DBContext()

    def add(self, event_model):
        session.add(event_model)
        session.commit()

    def get(self):
        pass

    def update(self):
        pass

    def deactivate(self):
        pass
