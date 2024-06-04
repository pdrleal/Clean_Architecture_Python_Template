from src.appservices.irepositories.ipeople_repo import IPeopleRepo
from src.appservices.iservices.ipeople_service import IPeopleService
from src.domain.people import People
from src.domain.profile import Profile
from src.dtos.people_dto import CreatePeopleInputDto


class PeopleService(IPeopleService):

    def __init__(self, people_repo: IPeopleRepo):
        self.people_repo = people_repo

    def create(self, dto: CreatePeopleInputDto):
        profile_model = Profile(email=dto.email, password=dto.password)
        people_model = People(first_name=dto.first_name, last_name=dto.last_name, active=False, profile=profile_model)

        self.people_repo.add(people_model)
        pass

    def get_all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
