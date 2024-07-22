
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.lable_text import TextWithLabel


class StoreView:
    def reset_form(self):
        status, store_list = StoreController.find_all()
        if status:
            for store in store_list:
                self.table.insert("", END, values=(store.product, store.inventory, store.category))

    def save_click(self):
        status, result = StoreController.save_store(self.product.get(), self.inventory.get(), self.category.get())
        if status:
            msg.showinfo("store saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("store View")
        self.win.geometry("1100x400")

        product = TextWithLabel(self.win, "product: ", 20, 20)

        inventory = TextWithLabel(self.win, "invetory: ", 20, 60)

        category = TextWithLabel(self.win, "national id: ", 20, 100)


        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

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