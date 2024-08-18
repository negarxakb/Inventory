
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.transaction_controller import TransactionController
from controller.product_controller import ProductController
from model.entity import transaction
from view.component.lable_text import TextWithLabel

class TransactionView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, transaction_list = TransactionController.find_all()
        if status:
            for transaction in transaction_list:
                self.table.insert("",END,values=(transaction.id,transaction.transaction_type,transaction.count,transaction.transaction_date_time))


    def save_click(self):
        status, result = TransactionController.save(self.transaction_type._variable.get(),self.count._variable.get(),self.transaction_date_time._variable.get())
        if status:
            entered_date = (
                f"transaction_Type: {self.transaction_type._variable.get()}\n"
                f"Count: {self.count._variable.get()}\n"
                f"Transaction_date_time: {self.transaction_date_time._variable.get()}"
            )
            msg.showinfo("Save", f"transaction saved? \n {entered_date}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)



    def edit_transaction(self):
        result=TransactionController.edit(self.id._variable.get(),self.product_id._variable.get(), self.transaction_type._variable.get(), self.count._variable.get())
        if result:
            entered_date = (
                    f"Id: {self.id._variable.get()}\n"
                    f"Product_id: {self.product_id._variable.get()}\n"
                    f"Type: {self.transaction_type._variable.get()}\n"
                    f"Count: {self.count._variable.get()}"
            )
            msg.showinfo("edit", f"transaction edited? \n {entered_date}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_transaction(self):
        id = self.remove_row._variable.get()
        TransactionController.remove(id)
        msg.showinfo("remove", f"transaction removed? \n {id}")
        self.reset_form()


    def find_product_by_id(self):
        get_id = self.find_product._variable.get()
        find_id = ProductController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Find", f"ProductId {get_id} delete?")
        else:
            msg.showerror("Error", f"ID {get_id} not found")


    def find_product_by_brand(self):
        get_brand=self.find_product._variable.get()
        find_brand = ProductController.find_by_brand
        if find_brand:
            msg.showinfo("Find", f"ProductId {get_brand} delete?")
        else:
            msg.showerror("Error", f"Brand {get_brand} not found")

            msg.showerror("Error", f"Brand {get_brand} not found")

    def show(self):
        self.win = Tk()
        self.win.title("transaction View")
        self.win.geometry("740x250")

        self.product_id = TextWithLabel(self.win, "product_id: ", 20, 20)

        self.transaction_type = TextWithLabel(self.win, "type: ", 20, 60)

        self.count = TextWithLabel(self.win, "count: ", 20, 100)



        Button(self.win, text="Search_id", command=self.find_product_by_id).place(x=140, y=150)

        Button(self.win, text="Search_brand", command=self.find_product_by_brand).place(x=220, y=150)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=150)

        Button(self.win, text="remove", command=self.remove_transaction).place(x=70, y=150)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4), show="headings")

        self.table.column(1, width=75)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)

        self.table.heading(1, text="product_id")
        self.table.heading(2, text="type")
        self.table.heading(3, text="count")
        self.table.heading(4, text="date_time")

        self.table.place(x=350, y=20)

        self.reset_form()

        self.win.mainloop()


