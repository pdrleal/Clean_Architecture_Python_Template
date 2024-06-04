from dependency_injector.wiring import inject, Provide
from flask import Blueprint

from application.dependency_container import DependencyContainer
from src.interfaceadapters.controllers.icontrollers.ipeople_controller import IPeopleController

people_blueprint = Blueprint('people-route', __name__)


@people_blueprint.route("/create", methods=["POST"])
@inject
def create(people_controller: IPeopleController = Provide[DependencyContainer.people_controller]):
    return people_controller.create()


@people_blueprint.route("/get_all", methods=["GET"])
@inject
def get_all(people_controller: IPeopleController = Provide[DependencyContainer.people_controller]):
    return people_controller.get_all()


@people_blueprint.route("/update", methods=["PUT"])
@inject
def update(people_controller: IPeopleController = Provide[DependencyContainer.people_controller]):
    return people_controller.update()


@people_blueprint.route("/delete", methods=["DELETE"])
@inject
def delete(people_controller: IPeopleController = Provide[DependencyContainer.people_controller]):
    return people_controller.delete()
