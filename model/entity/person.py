from sqlalchemy import Column, Integer, Boolean, String
from model.entity.base import *

class StoreOperation(Base):
    __tablename__ = "store_operation_tbl"
    _id = Column("id", Integer, primary_key=True,autoincrement=True)
    _buyer_name = Column("buyer_name",String(30))
    _buyer_family = Column("buyer_family")
    _national_id = Column("national_id",Integer)
    _address = Column("address",String(200))



    def __init__(self,id, buyer_name, buyer_family, national_id,address):
        self.id = id
        self.buyer_name = buyer_name
        self.buyer_family = buyer_family
        self.national_id = national_id
        self.address = address



    def get_id(self):
        return self._id

    def set_id(self,id):
        self._id = self


    def get_buyer_name(self):
        return self._buyer_name


    def set_buyer_name(self,buyer_name):
        self._buyer_name = buyer_name


    def get_buyer_family(self):
        return self


    def set_buyer_family(self,buyer_family):
        self._buyer_family=buyer_family


    def get_national_id(self):
        return self._national_id

    def set_national_id(self,national_id):
        self._national_id = national_id


    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address


    id = property(get_id,set_id)
    buyer_name = property(get_buyer_name,set_buyer_name)
    buyer_family = property(get_buyer_family,set_buyer_family)
    national_id = property(get_national_id,set_national_id)
    address = property(get_address,set_address)



