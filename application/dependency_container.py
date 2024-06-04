from dependency_injector import containers, providers

from src.appservices.event_service import EventService
from src.appservices.people_service import PeopleService
from src.infrastructure.persistence.dbcontext import DBContext
from src.interfaceadapters.controllers.event_controller import EventController
from src.interfaceadapters.controllers.people_controller import PeopleController
from src.interfaceadapters.repositories.event_repo import EventRepo
from src.interfaceadapters.repositories.people_repo import PeopleRepo


def setup_dependency_container(app, modules=None, packages=None):
    container = DependencyContainer()
    app.container = container
    app.container.wire(modules=modules, packages=packages)
    return app


class DependencyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration()

    db_context = providers.Factory(DBContext)

    # TODO: Provide the dependencies of each layer to inject.
    # Event

    event_repository = providers.Factory(EventRepo, db_context=db_context)
    event_service = providers.Factory(EventService, event_repo=event_repository)
    event_controller = providers.Factory(EventController, event_service=event_service)

    people_repository = providers.Factory(PeopleRepo, db_context=db_context)
    people_service = providers.Factory(PeopleService, people_repo=people_repository)
    people_controller = providers.Factory(PeopleController, people_service=people_service)
    # Project
    # project_repository = providers.Factory(ProjectRepo)
    # project_service = providers.Factory(ProjectService, project_repository=project_repository)
    # ...
