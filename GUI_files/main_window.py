from tkinter import *
from tkinter import ttk

from GUI_files.add_row_window import AddRowWindow
from GUI_files.remove_row_window import RemoveRowWindow
from GUI_files.add_column_window import AddColumnWindow
from GUI_files.remove_column_window import RemoveColumnWindow
from GUI_files.add_table_window import AddTableWindow
from GUI_files.remove_table_window import RemoveTableWindow
from GUI_files.filter_table_window import FilterTableWindow
from Parse import parse
from Logic import Database
from tkinter import filedialog
from json import dump

from copy import deepcopy


class MainWindow(Frame):
    def __init__(self, master, content):
        self.database = Database.Database()

        Frame.__init__(self, master)
        self.master = master
        self.content = content
        self.master.geometry("700x400+000+000")
        self.master['background'] = '#202020'

        self.get_data()

        self.popup_menu = Menu(self.master, tearoff=0)
        self.display_table = ttk.Treeview(self.master, height=10)

        self.add_row_button = Button(self.master)
        self.remove_row_button = Button(self.master)
        self.add_column_button = Button(self.master)
        self.remove_column_button = Button(self.master)
        self.add_table_button = Button(self.master)
        self.remove_table_button = Button(self.master)
        self.filter_table_button = Button(self.master)
        self.save_button = Button(self.master)

        self.list_box = Listbox(self.master)
        self.widgets()

    def get_data(self):
        parse.add_tables(self.database, self.content)
        parse.add_columns(self.database, self.content)
        parse.add_rows(self.database, self.content)

    def widgets(self):
        self.display_tables()

        self.list_box.config(width=10, height=15, bg='#493358', bd=0,
                             fg='#ffffff', relief='sunken', borderwidth=0, highlightthickness=0)

        self.display_content()

        self.add_row_button.config(text="Add row", width=15, height=2,
                                   command=lambda: self.create_new_window(AddRowWindow))
        self.add_row_button.place(x=70, y=28)

        self.remove_row_button.config(text="Remove row", width=15, height=2,
                                      command=lambda: self.create_new_window(RemoveRowWindow))
        self.remove_row_button.place(x=185, y=28)

        self.add_column_button.config(text="Add column", width=15, height=2,
                                      command=lambda: self.create_new_window(AddColumnWindow))
        self.add_column_button.place(x=300, y=28)

        self.remove_column_button.config(text="Remove column", width=15, height=2,
                                         command=lambda: self.create_new_window(RemoveColumnWindow))
        self.remove_column_button.place(x=415, y=28)

        self.add_table_button.config(text="Add\ntable", width=9, height=2,
                                     command=self.add_table)
        self.add_table_button.place(x=0, y=295)

        self.remove_table_button.config(text="Remove\ntable", width=9, height=2,
                                        command=self.remove_table)
        self.remove_table_button.place(x=72, y=295)

        self.filter_table_button.config(text="Filter table", width=15, height=2,
                                        command=lambda: self.create_new_window(FilterTableWindow))
        self.filter_table_button.place(x=530, y=28)

        self.save_button.config(text="Save\ndatabase", width=9, height=2,
                                command=self.save_table)
        self.save_button.place(x=144, y=295)

    def display_tables(self):
        self.list_box.delete(0, END)

        self.list_box.bind("<<ListboxSelect>>", self.display_content)

        self.list_box.place(x=0, y=28)
        self.list_box.config(font=("Arial", 10))

        tables = self.database.get_tables_names()

        for i, table in enumerate(tables):
            self.list_box.insert(i, table)

        self.list_box.select_set(0)

    def display_menu(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def display_content(self, event=0):
        selection = self.list_box.curselection()
        if selection:
            for item in self.display_table.get_children():
                self.display_table.delete(item)
            selection = self.list_box.get(selection[0])

            current_table_obj = self.database.get_active(selection)

            serialized_data = deepcopy(current_table_obj.get_rows())

            columns = current_table_obj.get_column_names()
            columns.insert(0, 'Lp.')
            for i, j in enumerate(serialized_data):
                j.insert(0, i)
            self.display_table['columns'] = columns

            for i in columns:
                self.display_table.heading(i, text=i, anchor='w')

            self.display_table.column('#0', width=0, stretch=NO)

            self.display_table.heading('#0', text='', anchor=CENTER)
            for i, j in enumerate(serialized_data):
                self.display_table.insert(parent='', index=i, values=j)
            self.display_table.place(x=70, y=68)

    def create_new_window(self, window_class):
        window_class(Toplevel(), self.get_current_table(), self)

    def add_table(self):
        AddTableWindow(Toplevel(), self.database, self)

    def remove_table(self):
        RemoveTableWindow(Toplevel(), self.database, self)

    def save_table(self):
        dump_dict = parse.get_json(self.database)
        file = filedialog.asksaveasfile(mode='w', defaultextension='.json')
        dump(dump_dict, file)

    def get_current_table(self):
        selection = self.list_box.curselection()
        selection = self.list_box.get(selection[0])
        if selection:
            return self.database.get_active(selection)
        else:
            self.list_box.select_set(0)
            self.get_current_table()
