import tkinter as tk

class InventoryApp:
 def __init__(self, root):
    self.root = root
    self.root.title("Inventory Management System")

    self.inventory = {
    "item1": 10,
    "item2": 20,
    "item3": 15
    }

    # self.create_widgets()

def create_widgets(self):
 self.item_list = tk.Listbox(self.root)
 for item in self.inventory:
    self.item_list.insert(tk.END, f"{item}: {self.inventory[item]}")
 self.item_list.pack()

 self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
 self.add_button.pack()
 self.remove_button = tk.Button(self.root, text="Remove Item", command=self.remove_item)
 self.remove_button.pack()

 def add_item(self):
    item_name = tk.simpledialog.askstring("Add Item", "Enter item name:")
    if item_name:
        item_quantity = tk.simpledialog.askinteger("Add Item", "Enter item quantity:")
    if item_quantity:
        self.update_list()

def remove_item(self):
    selected_index = self.item_list.curselection()
    if selected_index:
        item_name = self.item_list.get(selected_index)
        del self.inventory[item_name.split(":")[0].strip()]
        self.update_list()

def update_list(self):
    self.item_list.delete(0, tk.END)
    for item in self.inventory:
        self.item_list.insert(tk.END, f"{item}: {self.inventory[item]}")

root = tk.Tk()
app = InventoryApp(root)
root.mainloop()