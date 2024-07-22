from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.entity.product import Product


class Store(Base):
    __tablename__ = "store_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _count = Column("count", Integer)

    _product_id = Column("product_id", Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")

    #
    # def __init__(self, product, inventory, category):
    #     self._id = None
    #     self._product = product
    #     self._inventory = inventory
    #     self._category = category
    #
    # def get_id(self):
    #     return self._id
    #
    # def set_id(self, id):
    #     self._id = id
    #
    # def get_product(self):
    #     return self._product
    #
    # def set_product(self, product):
    #     self._product = product
    #
    # def get_inventory(self):
    #     return self._inventory
    #
    # def set_inventory(self, inventory):
    #     self._inventory = inventory
    #
    # def get_category(self):
    #     return self._category
    #
    # def set_category(self, category):
    #     self._category = category
    #
    # id = property(get_id, set_id)
    # product = property(get_product, set_product)
    # inventory = property(get_inventory, set_inventory)
    # category = property(get_category, set_category)
    #
