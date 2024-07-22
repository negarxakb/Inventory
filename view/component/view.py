from model.da.da import DataAccess
from view.component.lable_text import TextWithLabel
from view.component.table import Table
from model.entity.store import Store
from model.entity.person import Person
from model.entity.product import Product
from model.entity.transaction import Transaction
from tkinter import *

class PersonstoreView:
    def person_table_click(self,row):
        print (row)

    def store_table_click(self, row):
        print(row)

    def __init__(self):
        self.Person_da = DataAccess(Person)
        self.store_da = DataAccess(Store)
        self.win = Tk()
        self.title("Person Store View")
        self.win.geometry("500x500")

        person_table = Table(self.win,
                             ["Id", "Name", "Family", "NationalId", "address"],
                             [60,80,80,80,50], 20, 20 ,
                             self.person_table_click)

        self.person_table.refresh_table(self.person_da.find_all())
        store_table = Table(self.win,
                             ["Id","product","Inventory","category"],
                             [60,80,80,80],300,20 ,
                             self.store_table_click)

        self.win.mainloop()