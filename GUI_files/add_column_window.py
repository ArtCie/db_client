from tkinter import *
from Exceptions.Exceptions import WrongNameException
from Exceptions.Exceptions import ColumnNameAlreadyInTableException

from GUI_files.template import Template
from tkinter import messagebox
from Logic.Column import Column


class AddColumnWindow(Template):
    """Class represents add column window"""
    def __init__(self, master, active_table, parent):
        Template.__init__(self, master, active_table, parent, "500x100+200+200")
        self.value = StringVar(self.master)
        self.options = {"Integer number": "int",
                        "Float number": "float",
                        "Text": "str"}
        self.value.set("Text")
        self.choose_one = OptionMenu(self.master, self.value, *(self.options.keys()))
        self.label_choose = Label(self.master, text="Choose type", anchor="w", justify=LEFT)
        self.label_name = Label(self.master, text="Enter column name", anchor="w", justify=LEFT)
        self.entry_name = Entry(self.master)

        self.widgets()
        self.master.title("Add column")

        master.mainloop()

    def widgets(self):
        """Adjust details of widgets"""
        self.choose_one.grid(column=1, row=0, sticky=W)

        self.label_choose.place(x=20, y=20, width=140)
        self.label_name.place(x=160, y=20, width=120)
        self.entry_name.place(x=160, y=40, width=120, height=30)
        self.choose_one.place(x=20, y=40, width=140, height=30)

        self.button_accept.config(text="Ok", width=12, height=1,
                                  bg='#453d49',
                                  fg='#ffffff',
                                  relief='sunken',
                                  activebackground='#4f2b64',
                                  activeforeground='#ffffff',
                                  command=self.add)
        self.button_accept.place(x=300, y=70)
        self.button_cancel.config(text="Cancel", width=12, height=1,
                                  bg='#453d49',
                                  fg='#ffffff',
                                  relief='sunken',
                                  activebackground='#4f2b64',
                                  activeforeground='#ffffff',
                                  command=self.master.withdraw)
        self.button_cancel.place(x=400, y=70)

    def add(self):
        """Method checks if it is possible to create column with given name and adds it to table"""
        try:
            new_col = Column(eval(self.options[self.value.get()]), self.entry_name.get())
            self.active_table.add_column(new_col)

            self.parent.display_content()
            self.master.withdraw()
        except ColumnNameAlreadyInTableException as err:
            messagebox.showerror("Error", err)
        except WrongNameException as err:
            messagebox.showerror("Error", err)