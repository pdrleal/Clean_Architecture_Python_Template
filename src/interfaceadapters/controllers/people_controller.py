import json

from flask import Response, request

from src.appservices.iservices.ipeople_service import IPeopleService
from src.dtos.people_dto import CreatePeopleInputDto
from src.interfaceadapters.controllers.icontrollers.ipeople_controller import IPeopleController
from src.serializers.enhanced_json_encoder import EnhancedJSONEncoder


class PeopleController(IPeopleController):

    def __init__(self, people_service: IPeopleService) -> None:
        self.people_service = people_service

    def create(self):
        input_json = request.get_json()

        people_dto = CreatePeopleInputDto(email=input_json['email'], password=input_json['password'],
                                          first_name=input_json['first_name'], last_name=input_json['last_name'])
        result = self.people_service.create(people_dto)
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')

    def get_all(self):
        result = self.people_service.get_all()
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')

    def update(self):
        result = self.people_service.update()
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')

    def delete(self):
        result = self.people_service.delete()
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')
