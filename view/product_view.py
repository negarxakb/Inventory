
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.product_controller import ProductController
from view.component.lable_text import TextWithLabel


class ProductView:
    def reset_form(self):
        status, product_list = ProductController.find_all()
        if status:
            for product in product_list:
                self.table.insert("", END, values=(product.name, product.brand, product.price, product.description))

    def save_click(self):
        status, result = ProductController.save_product(self.name.get(), self.brand.get(), self.price.get(), self.description.get()))
        if status:
            msg.showinfo("product saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("product View")
        self.win.geometry("1100x400")

        name = TextWithLabel(self.win, "name: ", 20, 20)

        brand = TextWithLabel(self.win, "brand: ", 20, 60)

        price = TextWithLabel(self.win, "price: ", 20, 100)

        discription = TextWithLabel(self.win, "discription: ", 20, 140)



        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)



        self.table.heading(1, text="name")
        self.table.heading(2, text="brand")
        self.table.heading(3, text="price")
        self.table.heading(4, text="discription")


        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()