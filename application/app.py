from flask import Flask

from application.dependency_container import setup_dependency_container
from src.infrastructure.routes.event_blueprint import event_blueprint


def create_app(config_name, dependency_container_packages=None,
               dependency_container_modules=None, ):
    app = Flask(__name__)
    config_module = f"application.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)
    # TODO: Register Flask Blueprints
    app.register_blueprint(event_blueprint)
    # app.register_blueprint(project_blueprint)
    # ...
    app = setup_dependency_container(
        app,
        packages=dependency_container_packages,
        modules=dependency_container_modules
    )

    return app
