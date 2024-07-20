from sqlalchemy import Column, Integer, Boolean, String
from model.entity.base import *

class Product(Base):
    __tablename__ = "product_tbl"
    _id = Column("id",Integer,primary_key = True,autoincrement=True)
    _name = Column("name",String(20))
    _brand = Column("brand",String(40))
    _price = Column("price",Integer)
    _description = Column("description",String(100))


    def __init__(self,name,brand,price,description):
        self._id = None
        self._name = name
        self._brand = brand
        self._price = price
        self._description = description


    def get_id(self):
        return self._id

    def set_id(self,id):
        self._id = id


    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name


    def get_brand(self):
        return self._brand

    def set_brand(self,brand):
        self._brand = brand


    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price = price

    def get_description(self):
        return self._description

    def set_description(self,description):
        self._description = description



    id = property(get_id,set_id)
    name = property(get_name,set_name)
    brand = property(get_brand,set_brand)
    price = property(get_price,set_price)
    description = property(get_description,set_description)







