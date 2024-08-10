
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.product_controller import *
from view.component.lable_text import TextWithLabel
from model.entity import *


class ProductView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, product_list = ProductController.find_all()
        if status:
            for product in product_list:
                self.table.insert("", END, values=(product.name, product.brand, product.price, product.description))

    def save_click(self):
        print(self.name.get_variable())
        status, result = ProductController.save(self.name.get_variable(), self.brand.get_variable(), self.price.get_variable(), self.description.get_variable())
        if status:
            entered_data=(
                f"Name: {self.name.get_variable()}\n"
                f"Brand: {self.brand.get_variable()}\n"
                f"Price: {self.price.get_variable()}\n"
                f"Description: {self.description.get_variable()}"
            )

            msg.showinfo("Save", f"Account saved? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)


    def edit_product(self):
        result = ProductController.edit(self.name.get_variable(),self.brand.get_variable(),self.description.get_variable())
        if result:
            entered_data = (
                f"Name: {self.name.get_variable()}\n"
                f"Brand: {self.brand.get_variable()}\n"
                f"Description: {self.description.get_variable()}"
            )
            msg.showinfo("Edit", f"Name {entered_data} edited? \n")
            self.reset_form()
        elif result.startswith("False"):
            msg.showerror("Error", result)

    def remove_product(self):
        get_id = self.remove_row.get_variable()
        find_id = ProductController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"ProductId {get_id} delete?")
            ProductController.remove(get_id)
            self.reset_form()
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def show(self):
        self.win = Tk()
        self.win.title("product View")
        self.win.geometry("1100x500")

        self.name = TextWithLabel(self.win, "name: ", 20, 40)

        self.brand = TextWithLabel(self.win, "brand: ", 20, 80)

        self.price = TextWithLabel(self.win, "price: ", 20, 120)

        self.description = TextWithLabel(self.win, "discription: ", 20, 160)

        self.remove_row = TextWithLabel(self.win, "Remove Product By Id: ", 320, 280, distance=150)




        Button(self.win, text="save", command=self.save_click).place(x=500, y=330)

        Button(self.win, text="Edit", command=self.edit_product).place(x=550, y=330)

        Button(self.win, text="Remove", command=self.remove_product).place(x=600, y=330)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)



        self.table.heading(1, text="name")
        self.table.heading(2, text="brand")
        self.table.heading(3, text="price")
        self.table.heading(4, text="discription")


        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()
