from view import *
from tkinter import *
import tkinter.messagebox as msg

from view.person_view import PersonView
from view.product_view import ProductView
from view.store_view import StoreView
from view.transaction_view import TransactionView


class FrontView:

    def show_view_person(self):
        msg.showinfo("question", " مشخصات خود را وارد کنید ")
        ui = PersonView()
        ui.show()

    def show_view_product(self):
        ui = ProductView()
        ui.show()

    def show_view_store(self):
        ui = StoreView()
        ui.show()

    def show_view_transaction(self):
        ui = TransactionView()
        ui.show()


    def show(self):
        self.win = Tk()
        self.win.title("View")
        self.win.geometry("780x400")

        frame1 = Frame(self.win, bd=2, relief="sunken")
        frame1.place(x=50, y=50, width=300, height=250)

        frame2 = Frame(self.win, bd=2, relief="sunken")
        frame2.place(x=420, y=50, width=300, height=250)

        Label(frame1, text=".اگر حساب ندارید ابتدا حساب خود را ایجاد کنید ").pack(pady=20, padx=10)
        Button(frame1, text="ایجاد حساب", command=self.show_view_person).pack(pady=35)

        Label(frame2, text="در صورت داشتن حساب از موارد زیر استفاده کنید").pack(pady=20, padx=10)
        Button(frame2, text="محصول", command=self.show_view_product).pack(pady=10)
        Button(frame2, text="ایجاد تراکنش", command=self.show_view_transaction).pack(pady=10)
        Button(frame2,text="انبار", command=self.show_view_store).pack(pady=10)

        self.win.mainloop()


ui = FrontView()
ui.show()







