from src.appservices.irepositories.ievent_repo import IEventRepo
from src.infrastructure.persistence.dbcontext import DBContext


class EventRepo(IEventRepo):

    def __init__(self, db_context: DBContext):
        self.db_context = db_context

    def add(self, event):
        with self.db_context.Session() as session:
            session.add(event)
            session.commit()

    def get(self):
        pass

    def update(self):
        pass

    def deactivate(self):
        pass
