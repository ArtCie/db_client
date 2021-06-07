from tkinter import *
from copy import deepcopy


class Template(Frame):
    """Class has repeatable methods for all windows"""
    def __init__(self, master, active_table, parent, size):
        """Takes master window, active table, parent object and its size"""
        Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.active_table = active_table
        self.enter_values = []
        self.grid()
        self.menubar = Menu(master)
        self.button_accept = Button(master)
        self.button_cancel = Button(master)

        self.master['background'] = '#202020'
        self.master.geometry(size)

    @staticmethod
    def display_table(display_table, active_table):
        """Method takes ttk.treeview object and inserts elements from active table object to it"""
        serialized_data = deepcopy(active_table.get_rows())

        columns = active_table.get_column_names()
        columns.insert(0, 'Lp.')
        for i, j in enumerate(serialized_data):
            j.insert(0, i)
        display_table['columns'] = columns
        for i in range(len(display_table['columns'])):
            display_table.column(f'#{i+1}', width=80)

        for i in columns:
            display_table.heading(i, text=i, anchor='w')

        display_table.column('#0', width=0, stretch=NO)

        display_table.heading('#0', text='', anchor=CENTER)
        for i, j in enumerate(serialized_data):
            display_table.insert(parent='', index=i, values=j)