from model.entity import *





class Store(Base):
    __tablename__ = "store_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _inventory = Column("inventory", Integer)

    _product_id = Column("product_id", Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")


    def __init__(self,product,inventory,product_id):
         self.id = None
         self.product = product
         self.inventory = inventory
         self.product_id = product_id





    def get_id(self):
        return self._id

    def set_id(self, id):
         self._id = id

    def get_inventory(self):
         return self._inventory

    def set_inventory(self, inventory):
         self._inventory = inventory

    def get_product_id(self):
         return self._product_id

    def set_product_id(self,product_id ):
         self._product_id = product_id

    # def get_category(self):
    #     return self._category
    #
    # def set_category(self, category):
    #     self._category = category
    #
    id= property(get_id, set_id)
    inventory= property(get_inventory, set_inventory)
    product_id= property(get_product_id, set_product_id)
    # category = property(get_category, set_category)
    #
