from tkinter import *
from tkinter import ttk

from GUI_files.template import Template
from tkinter import messagebox
from Logic.Table import Table
from Logic.Column import Column


class RemoveTableWindow(Frame):
    """Class represents window to remove tables"""
    def __init__(self, master, database, parent):
        """Constructor defines variables - buttons, ttk.Treeview objects and runs mainloop"""
        Frame.__init__(self, master)

        self.database = database
        self.parent = parent

        self.master.title("Remove tables")

        self.display_table = ttk.Treeview(self.master, selectmode='extended')
        self.display_table.place(x=20, y=20)

        self.remove_data = ttk.Treeview(self.master, selectmode='extended')
        self.remove_data.place(x=260, y=20)

        self.button_right = Button(master)
        self.button_left = Button(master)

        self.button_accept = Button(master)
        self.button_cancel = Button(master)

        self.widgets()
        master.mainloop()

    def widgets(self):
        """Adjust details of widgets"""
        self.display_tables()

        self.button_right.config(text="=>", width=4, height=2,
                                 command=lambda: Template.move(self.remove_data, self.display_table))
        self.button_right.place(x=200, y=80)
        self.button_left.config(text="<=", width=4, height=2,
                                command=lambda: Template.move(self.display_table, self.remove_data))
        self.button_left.place(x=200, y=150)

        self.master.geometry("470x350+200+200")
        self.master.title("Remove table")
        self.master['background'] = '#202020'

        self.button_accept.config(text="Delete", width=15, height=2, command=self.accept_window)
        self.button_accept.place(x=174, y=260)
        self.button_cancel.config(text="Cancel", width=15, height=2, command=self.master.withdraw)
        self.button_cancel.place(x=298, y=260)

    def accept_window(self):
        """Method defines messagebox asking user if he is certain to delete tables"""
        msg_box = messagebox.askquestion('Delete tables', 'Are you sure you want to delete these tables?', icon='warning')
        if msg_box == 'yes':
            self.remove()

    def remove(self):
        """Method removes table from database"""
        for i in self.remove_data.get_children():
            item = self.remove_data.item(i)['values'][1:]
            self.database.remove_table(self.database.get_active(item[0]))
        self.parent.display_tables()
        self.master.withdraw()

    def display_tables(self):
        """Method to display both ttk.treeview tables"""
        first_row = ['Lp.', 'Table name']
        self.display_table['columns'] = first_row
        self.remove_data['columns'] = first_row

        for i in first_row:
            self.display_table.heading(i, text=i, anchor='w')
            self.remove_data.heading(i, text=i, anchor='w')

        self.set_cols_size('#1', 30)
        self.set_cols_size('#2', 120)
        self.set_cols_size('#0', 0)

        columns = self.database.get_tables_names()

        for i, j in enumerate(columns):
            self.display_table.insert(parent='', index=i, values=[i, j])

    def set_cols_size(self, index, num):
        """Method sets size of columns"""
        self.display_table.column(index, width=num, stretch=NO)
        self.remove_data.column(index, width=num, stretch=NO)