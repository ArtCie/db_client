from tkinter import *
from tkinter import messagebox
from Exceptions.Exceptions import WrongNameException
from Exceptions.Exceptions import TableNameAlreadyInDatabaseException

from Logic.Table import Table


class AddTableWindow(Frame):
    """Class represents add table window"""
    def __init__(self, master, database, parent):
        Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.database = database
        self.entry_name = Entry(self.master)
        self.button_accept = Button(master)
        self.button_cancel = Button(master)
        self.label_name = Label(self.master, text="Enter table name", anchor="w", justify=LEFT)
        self.widgets()

        master.mainloop()

    def widgets(self):
        """Adjust details of widgets"""
        self.master.title("Add table")
        self.master['background'] = '#202020'
        self.master.geometry("350x100+200+200")

        self.label_name.place(x=20, y=16, width=120)
        self.entry_name.place(x=20, y=30, width=120, height=30)

        self.button_accept.config(text="Ok", width=12, height=1,
                                  bg='#453d49',
                                  fg='#ffffff',
                                  relief='sunken',
                                  activebackground='#4f2b64',
                                  activeforeground='#ffffff',
                                  command=self.add)
        self.button_accept.place(x=140, y=70)

        self.button_cancel.config(text="Cancel", width=12, height=1,
                                  bg='#453d49',
                                  fg='#ffffff',
                                  relief='sunken',
                                  activebackground='#4f2b64',
                                  activeforeground='#ffffff',
                                  command=self.master.withdraw)
        self.button_cancel.place(x=240, y=70)

    def add(self):
        """Method takes what was written by user and creates new table"""
        try:
            self.database.add_table(Table(self.entry_name.get()))
        except TableNameAlreadyInDatabaseException as err:
            messagebox.showerror("Error", err)
        except WrongNameException as err:
            messagebox.showerror("Error", err)
        self.parent.display_tables()
        self.master.withdraw()
