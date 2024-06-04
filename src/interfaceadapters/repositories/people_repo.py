from src.appservices.irepositories.ipeople_repo import IPeopleRepo
from src.infrastructure.persistence.dbcontext import DBContext


class PeopleRepo(IPeopleRepo):

    def __init__(self, db_context: DBContext):
        self.db_context = db_context

    def add(self, model):
        with self.db_context.Session() as session:
            session.add(model)
            session.commit()

    def get(self):
        pass

    def update(self):
        pass

    def deactivate(self):
        pass
