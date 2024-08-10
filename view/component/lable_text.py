from tkinter import StringVar, Label, Entry


class TextWithLabel:
    def __init__(self, master, text, x, y, distance=80, disabled=False):
        self._variable = StringVar(master)

        Label(master, text=text).place(x=x, y=y)

        if disabled:
            text_box = Entry(master, textvariable=self._variable, state="readonly")
            text_box.place(x=x + distance, y=y)
        else:
            text_box = Entry(master, textvariable=self._variable,)
            text_box.place(x=x + distance, y=y)

    def get_variable(self):
        return self._variable.get()

    def set_variable(self, variable):
        self._variable.set(variable)

    text = property(get_variable, set_variable)