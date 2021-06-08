from tkinter import *
from tkinter import ttk

from GUI_files.template import Template
from tkinter import messagebox
from Logic.Column import Column


class RemoveColumnWindow(Template):
    """Class that represents remove column window"""
    def __init__(self, master, active_table, parent):
        Template.__init__(self, master, active_table, parent, "670x500+200+200")

        self.master.title("Remove columns")

        self.display_table = ttk.Treeview(self.master, selectmode='extended')
        self.display_table.place(x=20, y=20)

        self.remove_data = ttk.Treeview(self.master, selectmode='extended')
        self.remove_data.place(x=365, y=20)

        self.button_right = Button(master)
        self.button_left = Button(master)

        self.button_accept = Button(master)
        self.button_cancel = Button(master)

        self.widgets()
        master.mainloop()

    def widgets(self):
        """Adjust details of widgets"""
        self.display_columns()

        self.button_right.config(text="=>", width=4, height=2,
                                 command=lambda: Template.move(self.remove_data, self.display_table))
        self.button_right.place(x=310, y=80)
        self.button_left.config(text="<=", width=4, height=2,
                                command=lambda: Template.move(self.display_table, self.remove_data))
        self.button_left.place(x=310, y=150)

        self.button_accept.config(text="Delete", width=15, height=2, command=self.accept_window)
        self.button_accept.place(x=390, y=400)
        self.button_cancel.config(text="Cancel", width=15, height=2, command=self.master.withdraw)
        self.button_cancel.place(x=520, y=400)

    def accept_window(self):
        """Method calls window to ask user if he is certain to remove columns."""
        msg_box = messagebox.askquestion('Delete columns', 'Are you sure you want to delete these columns?', icon='warning')
        if msg_box == 'yes':
            self.remove()

    def remove(self):
        """Method removes selected columns from table"""
        map_types = {
            "Tekst": str,
            "Liczba całkowita": int,
            "Liczba rzeczywista": float
        }
        for i in self.remove_data.get_children():
            item = self.remove_data.item(i)['values'][1:]
            remove_item = self.active_table.get_col(Column(map_types[item[1]], item[0]))
            self.active_table.remove_column(remove_item)
        self.parent.display_content()
        self.master.withdraw()


    def display_columns(self):
        first_row = ['Lp.', 'Column name', 'Type']
        self.display_table['columns'] = first_row
        self.remove_data['columns'] = first_row

        for i in first_row:
            self.display_table.heading(i, text=i, anchor='w')
            self.remove_data.heading(i, text=i, anchor='w')

        self.set_cols_size('#1', 30)
        self.set_cols_size('#2', 120)
        self.set_cols_size('#3', 120)
        self.set_cols_size('#0', 0)

        map_types = {
            str: "Tekst",
            int: "Liczba całkowita",
            float: "Liczba rzeczywista"
        }
        columns = self.active_table.get_column_names()
        table_types = self.active_table.get_column_types()
        for i, j in enumerate(columns):
            self.display_table.insert(parent='', index=i, values=[i, j, map_types[table_types[i]]])

    def set_cols_size(self, index, num):
        self.display_table.column(index, width=num, stretch=NO)
        self.remove_data.column(index, width=num, stretch=NO)