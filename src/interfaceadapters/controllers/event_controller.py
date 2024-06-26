import json

from flask import Response, request

from src.appservices.iservices.ievent_service import IEventService
from src.dtos.event_dto import CreateEventInputDto
from src.dtos.location_dto import CreateLocationInputDto
from src.interfaceadapters.controllers.icontrollers.ievent_controller import IEventController
from src.serializers.enhanced_json_encoder import EnhancedJSONEncoder


class EventController(IEventController):

    def __init__(self, event_service: IEventService) -> None:
        self.event_service = event_service

    def create(self):
        input_json = request.get_json()
        event_dto = CreateEventInputDto(name=input_json['name'], recurring=input_json['recurring'],
                                        event_type=input_json['event_type'],
                                        start_datetime=input_json['start_datetime'],
                                        end_datetime=input_json['end_datetime'],
                                        location=CreateLocationInputDto(address=input_json['location']['address'],
                                                                        city=input_json['location']['city'],
                                                                        country=input_json['location']['country']))
        result = self.event_service.create(event_dto)
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')

    def get_all(self):
        result = self.event_service.get_all()
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')

    def update(self):
        result = self.event_service.update()
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')

    def delete(self):
        result = self.event_service.delete()
        return Response(json.dumps(result, cls=EnhancedJSONEncoder), mimetype='application/json')
