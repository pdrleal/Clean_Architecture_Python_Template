from dependency_injector.wiring import inject, Provide
from flask import Blueprint, request

from application.dependency_container import DependencyContainer
from src.interfaceadapters.controllers.icontrollers.ievent_controller import IEventController

event_blueprint = Blueprint('event-route', __name__)


@event_blueprint.route("/create", methods=["POST"])
@inject
def create_event(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.create_event()


@event_blueprint.route("/get", methods=["GET"])
@inject
def get_events(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.get_events()


@event_blueprint.route("/update", methods=["PUT"])
@inject
def update_event(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.update_event()


@event_blueprint.route("/delete", methods=["DELETE"])
@inject
def delete_event(event_controller: IEventController = Provide[DependencyContainer.event_controller]):
    return event_controller.delete_event()
