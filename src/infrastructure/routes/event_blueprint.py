from dependency_injector.wiring import inject, Provide
from flask import Blueprint

from application.dependency_container import DependencyContainer
from src.interfaceadapters.controllers.icontrollers.ievent_controller import IEventController

event_blueprint = Blueprint('event-route', __name__)


@event_blueprint.route("/create", methods=["POST"])
@inject
def create(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.create()


@event_blueprint.route("/get_all", methods=["GET"])
@inject
def get_all(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.get_all()


@event_blueprint.route("/update", methods=["PUT"])
@inject
def update(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.update()


@event_blueprint.route("/delete", methods=["DELETE"])
@inject
def delete(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.delete()
