from model.entity import *

class Transaction(Base):
    __tablename__ = "transaction_tbl"
    _id = Column("id",Integer, primary_key = True,autoincrement=True)
    _transaction_type = Column("transaction_type",String(6))
    _count = Column("count",Integer)
    _transaction_date_time = Column("transaction_date_time", DateTime, nullable=False)

    _product_id = Column("product_id",Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")

    _person_id = Column("person_id",Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")


    def __init__(self,transaction_type,count,transaction_date_time):
        self.id = None
        self.product_id =None
        self.transaction_type =transaction_type
        self.count = count
        self.transaction_date_time = transaction_date_time
        self.person_id = None


    def get_id(self):
        return self._id

    def set_id(self,id):
         self._id = id


    def get_product_id(self):
         return self._product_id

    def set_product_id(self,product_id):
         self._product_id = product_id


    def get_transaction_type(self):
         return self._transaction_type

    def set_transaction_type(self,transaction_type):
         self._transaction_type =transaction_type


    def get_count(self):
         return self._count

    def set_count(self,count):
         self._count = count


    def get_transaction_date_time(self):
         return self._transaction_date_time

    def set_transaction_date_time(self,date_time):
         self._transaction_date_time= date_time



    id =property(get_id,set_id)
    product_id =property(get_product_id,set_product_id)
    transaction_type =property(get_transaction_type,set_transaction_type)
    count =property(get_count,set_count)
    transaction_date_time=property(get_transaction_date_time,set_transaction_date_time)

