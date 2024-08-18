
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.transaction_view import TransactionView

from controller.store_controller import StoreController
from view.component.lable_text import TextWithLabel


class StoreView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, store_list = StoreController.find_all()
        if status:
            for store in store_list:
                self.table.insert("", END, values=(store.product, store.inventory, store.product_id))

    def show_transaction(self):
        ui = TransactionView()
        ui.show()




    def show(self):
        self.win = Tk()
        self.win.title("store View")
        self.win.geometry("350x300")

        self.table = ttk.Treeview(self.win, columns=(1,2,3), show="headings")
        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)

        self.table.heading(1, text="product")
        self.table.heading(2, text="inventory")
        self.table.heading(3, text="product_id")


        self.table.place(x=20,y=20)

        self.reset_form()

        self.win.mainloop()

