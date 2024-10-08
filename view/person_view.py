from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.person_controller import PersonController
from view.component.lable_text import TextWithLabel


class PersonView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, person_list = PersonController.find_all()
        if status:
            for person in person_list:
                self.table.insert("", END, values=(person.buyer_name, person.buyer_family, person.national_id, person.address))

    def save_click(self):
        status, result = PersonController.save(self.buyer_name._variable.get(), self.buyer_family._variable.get(), self.national_id._variable.get(),self.address._variable.get())
        if status:
            entered_data=(
                f"Buyer_Name: {self.buyer_name._variable.get()}\n"
                f"Buyer_Family: {self.buyer_family._variable.get()}\n"
                f"National ID: {self.national_id._variable.get()}\n"
                f"Address: {self.address._variable.get()}"
            )
            msg.showinfo("Save!",f"save Person?\n{entered_data}")
            msg.showinfo("Question", "مشخصات شما سیو شد. برای ساخت حساب کار بری روی دکمه ی create account کلیک کنید.")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)



    def edit_person(self):
        result = PersonController.edit(self.buyer_name._variable.get(), self.buyer_family._variable.get(),self.national_id._variable.get(), self.address._variable.get())

        if result:
            entered_data = (
                f"Buyer_Name: {self.buyer_name._variable.get()}\n"
                f"Buyer_Family: {self.buyer_family._variable.get()}\n"
                f"National ID: {self.national_id._variable.get()}\n"
                f"Address: {self.address._variable.get()}"

            )
            msg.showinfo("Edit", f"Edit person? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_person(self):
        id = self.remove_row._variable.get()
        PersonController.remove(id)
        msg.showinfo("Remove", f"Remove person? \n {id}")
        self.reset_form()




    def show(self):
        self.win = Tk()
        self.win.title("person View")
        self.win.geometry("700x250")

        self.buyer_name = TextWithLabel(self.win, "name: ", 20, 20)

        self.buyer_family = TextWithLabel(self.win, "family: ", 20, 60)

        self.national_id = TextWithLabel(self.win, "national id: ", 20, 100)

        self.address = TextWithLabel(self.win, "address: ", 20, 140)


        self.remove_row = TextWithLabel(self.win, "ID For Remove :", 20, 260,distance=100)


        Button(self.win, text="save", command=self.save_click).place(x=20, y=200)

        Button(self.win, text="edit", command=self.edit_person).place(x=80, y=200)

        Button(self.win, text="remove", command=self.remove_person).place(x=140, y=200)


        self.table = ttk.Treeview(self.win, columns=(1,2,3,4), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)



        self.table.heading(1, text="name")
        self.table.heading(2, text="family")
        self.table.heading(3, text="national id")
        self.table.heading(4, text="address")


        self.table.place(x=280,y=20)

        self.reset_form()

        self.win.mainloop()
