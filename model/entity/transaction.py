from sqlalchemy import Column, Integer, Boolean, String,DateTime, ForeignKey
from model.entity.base import *

class Transaction(Base):
    __tablename__ = "transaction_tbl"
    _id = Column("id",Integer, primary_key = True,autoincrement=True)
    _product_id = Column("product_id",Integer)
    _type = Column("type",String(5))
    _count = Column("count",Integer)
    # _date_time = Column("date_time",Date)
    _date_time = Column("date_time", DateTime, nullable=False)

    def __init__(self,id,product_id,type,count,date_time):
        self.id = id
        self.product_id =product_id
        self.type = type
        self.count = count
        self.date_time = date_time


    def get_id(self):
        return self._id

    def set_id(self,id):
        self._id = id


    def get_product_id(self):
        return self._product_id

    def set_product_id(self,product_id):
        self._product_id = product_id


    def get_type(self):
        return self._type

    def set_type(self,type):
        self._type = type


    def get_count(self):
        return self._count

    def set_count(self,count):
        self._count = count


    def get_date_time(self):
        return self._date_time

    def set_date_time(self,date_time):
        self._date_time = date_time



    id =property(get_id,set_id)
    product_id =property(get_product_id,set_product_id)
    type =property(get_type,set_type)
    count =property(get_count,set_count)
    date_time =property(get_date_time,set_date_time)





