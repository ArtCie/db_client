from tkinter import *

from GUI_files.template import Template
from tkinter import messagebox
from Logic.Column import Column


class AddColumnWindow(Template):
    def __init__(self, master, active_table, parent):
        Template.__init__(self, master, active_table, parent, "500x100+200+200")
        self.value = StringVar(self.master)
        self.options = {"Liczba całkowita": "int",
                        "Liczba rzeczywista": "float",
                        "Tekst": "str"}
        self.value.set("Tekst")
        self.choose_one = OptionMenu(self.master, self.value, *(self.options.keys()))
        self.label_choose = Label(self.master, text="Choose type", anchor="w", justify=LEFT)
        self.label_name = Label(self.master, text="Enter column name", anchor="w", justify=LEFT)
        self.entry_name = Entry(self.master)

        self.widgets()
        self.master.title("Add column")

        master.mainloop()

    def widgets(self):

        self.choose_one.grid(column=1, row=0, sticky=W)

        self.label_choose.place(x=20, y=20, width=140)
        self.label_name.place(x=160, y=20, width=120)
        self.entry_name.place(x=160, y=40, width=120, height=30)
        self.choose_one.place(x=20, y=40, width=140, height=30)

        self.button_accept.config(text="Ok", width=12, height=1, command=self.add)
        self.button_accept.place(x=300, y=70)
        self.button_cancel.config(text="Cancel", width=12, height=1, command=self.master.withdraw)
        self.button_cancel.place(x=400, y=70)

    def add(self):
        try:
            new_col = Column(eval(self.options[self.value.get()]), self.entry_name.get())
            self.active_table.add_column(new_col)

            self.parent.display_content()
            self.master.withdraw()
        except AssertionError:
            messagebox.showerror("Error", "Name of column must be unique!")
        except ValueError:
            messagebox.showerror("Error", "Cannot add column with empty name!")