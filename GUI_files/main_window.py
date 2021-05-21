from tkinter import *
from tkinter import ttk

from GUI_files.pop_up_window import PopUpWindow
from db_operations import get_tables, get_data, get_columns_names


class MainWindow(Frame):
    def __init__(self, master, content):
        Frame.__init__(self, master)
        self.master = master
        self.content = content
        self.master.geometry("1000x1200+000+000")
        self.master['background'] = '#202020'

        self.popup_menu = Menu(self.master, tearoff=0)
        self.display_table = ttk.Treeview(self.master)

        self.add_button = Button(self.master)
        self.list_box = Listbox(self.master)
        self.widgets()

    def widgets(self):
        tables = get_tables(self.content)
        self.display_tables(tables)

        self.list_box.config(width=10, height=1030, bg='#493358', bd=0,
                             fg='#ffffff', relief='sunken', borderwidth=0, highlightthickness=0)

        self.display_content()

        self.add_button.config(text=("Insert into " + "table"), width=12, height=2, command=self.add_to_base)
        self.add_button.place(x=70, y=20)

    def display_tables(self, tables):

        self.popup_menu.add_command(label="hej")
        self.popup_menu.add_command(label="hej2")

        self.list_box.bind("<<ListboxSelect>>", self.display_content)

        self.list_box.place(x=0, y=20)
        self.list_box.config(font=("Arial", 10))
        for i, table in enumerate(tables):
            self.list_box.insert(i, table)

        self.list_box.select_set(0)
        self.list_box.bind("<Button-3>", self.display_menu)

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
            serialized_data = get_data(self.content[selection])
            columns = get_columns_names(self.content[selection])
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
            self.display_table.place(x=70, y=60)

    def add_to_base(self):
        pop_up = Toplevel()
        selection = self.list_box.curselection()
        selection = self.list_box.get(selection[0])

        app = PopUpWindow(pop_up, self.content, selection, self)