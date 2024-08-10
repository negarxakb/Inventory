
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.store_controller import StoreController
from view.component.lable_text import TextWithLabel


class StoreView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, store_list = StoreController.find_all()
        if status:
            for store in store_list:
                self.table.insert("", END, values=(store.product, store.inventory, store.category))

    def save_click(self):
        status, result = StoreController.save(self.product.get(), self.inventory.get(), self.category.get())
        if status:
            entered_data = (
                f"product:{self.product.get()}\n"
                f"inventory:{self.inventory.get()}\n"
                f"category:{self.category.get()}"
            )
            msg.showinfo("store saved!", f"Store saved?\n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)


    def edit(self):
        result = StoreController.edit(self.product.get(),self.inventory.get(),self.category.get())
        if result:
            entered_data = (
                f"product:{self.product.get()}\n"
                f"inventory:{self.inventory.get()}\n"
                f"category:{self.category.get()}"
            )

            msg.showinfo("Edit", f"store {entered_data} edited? \n")
            self.reset_form()
        elif result.startswith("False"):
            msg.showerror("Error", result)


    def remove(self):
        get_id = self.remove_row.get()
        find_id = StoreController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"StoreId {get_id} delete?")
            StoreController.remove(get_id)
            self.reset_form()
        else:
            msg.showerror("Error", f"ID {get_id} not found")


     #def find_by_category(self):




    def show(self):
        self.win = Tk()
        self.win.title("store View")
        self.win.geometry("1100x400")

        self.product = TextWithLabel(self.win, "product: ", 20, 20)

        self.inventory = TextWithLabel(self.win, "invetory: ", 20, 60)

        self.category = TextWithLabel(self.win, "national id: ", 20, 100)


        self.remove_row = TextWithLabel(self.win, "Remove Account By Id: ", 300, 300, distance=150)



        Button(self.win, text= "save", command=self.save_click).place(x=300 , y=350)
        Button(self.win, text="Edit", command=self.edit).place(x=350, y=350)
        Button(self.win, text="Remove", command=self.remove).place(x=400, y=350)

        self.table = ttk.Treeview(self.win, columns=(1,2,3), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)



        self.table.heading(1, text="product")
        self.table.heading(2, text="inventory")
        self.table.heading(3, text="category")


        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()