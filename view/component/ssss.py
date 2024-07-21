from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter import *
import tkinter.ttk
import tkinter.messagebox



def __init__(root):
    root = root

    root.title("My Store")

    root.geometry("1250x650")

    item_name_label = Label(root, text="نام محصول:")
    item_name_label.pack()
    item_name_entry = Entry(root)
    item_name_entry.pack()

    quantity_label = Label(root, text="تعداد:")
    quantity_label.pack()
    quantity_entry = Entry(root)
    quantity_entry.pack()

    add_button = Button(root, text="افزودن محصول", command=root.add_item)
    add_button.pack()

    remove_button = Button(root, text="حذف محصول", command=remove_item)




messagebox.showinfo("عملیات موفق", "محصول با موفقیت به انبار اضافه شد!")

def remove_item(self):
   item_name = item_name_entry.get()



messagebox.showinfo("عملیات موفق", "محصول با موفقیت از انبار حذف شد!")

root = Tk()



root.mainloop()