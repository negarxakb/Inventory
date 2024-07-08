from sqlalchemy import Column, Integer, Boolean, String
from model.entity.base import *
class Store(Base):
    __tablename__ = "store_tbl"
    _id = Column("id",Integer,primary_key = True,autoincrement=True)
    _product = Column("product",String(20))
    _inventory = Column("inventory",Integer)
    _shelving = Column("shelving",String(40))

    def __init__(self,id, product, inventory, shelving):
         self.id = None
         self.product = product
         self.inventory = inventory
         self.shelving = shelving

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_product(self):
        return self._product

    def set_product(self, product):
        self._product = product

    def get_inventory(self):
         return self._inventory

    def set_inventory(self, inventory):
         self._inventory = inventory

    def get_shelving(self):
         return self._shelving

    def set_shelving(self, shelving):
         self._shelving = shelving



    id = property(get_id, set_id)
    product = property(get_product, set_product)
    inventory = property(get_inventory, set_inventory)
    shelving = property(get_shelving, set_shelving)






