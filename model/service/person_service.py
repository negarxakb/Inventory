from controller.exceptions.exception import PersonNotFoundError
from model.da.da import DataAccess
from model.entity.person import Person

class PersonService:
    @staticmethod
    def save(person):
        person_da = DataAccess(person)
        person_da.save(person)
        return person

    @staticmethod
    def edit(person):
        person_da = DataAccess(person)
        person_da.save(person)
        return person

    @staticmethod
    def remove(id):
        person_da = DataAccess(Person)
        if  person_da.find_by_id(id):
            return person_da.remove(id)
        else:
            raise PersonNotFoundError



    @staticmethod
    def find_by_id(id):
        person_da = DataAccess(Person)
        if person_da.find_by_id(id):
            return person_da.find_by_id(id)


    @staticmethod
    def find_by_name(name):
        person_da = DataAccess(Person)
        return person_da.find_by(name)

    @staticmethod
    def find_by_family(family):
        person_da = DataAccess(Person)
        return person_da.find_by(family)






