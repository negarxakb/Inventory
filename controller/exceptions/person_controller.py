from model.entity.person import Person
from model.service.person_service import PersonService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger


class PersonController:

    @classmethod
    @exception_handling
    def save(cls, buyer_name,buyer_family,national_id,address):
        person = Person(buyer_name,buyer_family,national_id,address)
        PersonService.save(person)
        return True,person


    @classmethod
    @exception_handling
    def edit(cls,id,buyer_name,buyer_family,national_id,address):
        person = Person(id,buyer_name,buyer_family,national_id,address)
        PersonService.edit(person)
        return True, person



    @classmethod
    @exception_handling
    def remove(cls, id):
        person = PersonService.remove(id)
        Logger.info(f"Person Removed - {person}")
        return True, person


    @classmethod
    @exception_handling
    def find_all(cls,):
        person_list = PersonService.find_all()
        Logger.info(f"Person Find  BY  Id({id})")
        return True,person_list


    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        person = PersonService.find_by_id(id)
        Logger.info(f"Person Find  BY  Id({id})")
        return True,person


    @classmethod
    @exception_handling
    def find_by_buyer_name(cls,buyer_name):
        person =  PersonService.find_by_buyer_name(buyer_name)
        Logger.info(f"Person Find  BY  BuyerName({buyer_name})")
        return True,person


    @classmethod
    @exception_handling
    def find_by_buyer_family(cls,buyer_family):
        person =  PersonService.find_by_buyer_name(buyer_family)
        Logger.info(f"Person Find  BY  BuyerFamily({buyer_family})")
        return True,person









