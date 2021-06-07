from tkinter import messagebox
from copy import deepcopy

from tkinter import *
from tkinter import ttk


class FilterTableWindow(Frame):
    """Class represents window to filter table"""
    def __init__(self, master, active_table, parent):
        Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.result_table = []
        self.active_table = deepcopy(active_table)
        self.entry_lambda = Entry(self.master)
        self.button_filter = Button(master)
        self.button_cancel = Button(master)
        self.label_name = Label(self.master, text="Type lambda expression", anchor="w", justify=LEFT)

        self.display_table = ttk.Treeview(self.master, selectmode='extended')
        self.display_table.place(x=20, y=80)

        self.widgets()

        master.mainloop()

    def widgets(self):
        """Adjust details of widgets"""
        self.master.title("Filter table")
        self.master['background'] = '#202020'
        self.master.geometry("780x380+200+200")

        self.label_name.place(x=20, y=16, width=440)
        self.entry_lambda.place(x=20, y=30, width=440, height=30)
        self.entry_lambda.insert(0, "lambda row: row['Col1'] operator val and/or row['Col2'] operator val")

        self.button_filter.config(text="Filter", width=12, height=2, command=self.filter_table)
        self.button_filter.place(x=667, y=80)

        self.button_cancel.config(text="Finish", width=12, height=2, command=self.master.withdraw)
        self.button_cancel.place(x=667, y=320)

        self.display_tables()

    def filter_table(self):
        """Method takes expression typed by user and tries to parse it"""
        try:
            self.result_table = []
            lambda_expression = self.entry_lambda.get()
            print(lambda_expression)
            rows = self.active_table.query(lambda_expression)
            for i in rows:
                self.result_table.append(i)

            self.display_tables()

        except SyntaxError:
            messagebox.showerror("Error", "Syntax error")

    def display_tables(self):
        """Method display result table"""
        for item in self.display_table.get_children():
            self.display_table.delete(item)

        columns = self.active_table.get_column_names()
        columns.insert(0, 'Lp.')

        for i, j in enumerate(self.result_table):
            j.insert(0, i)
        self.display_table['columns'] = columns
        # for i in range(0, len(self.display_table['columns'])):
        #     self.display_table.column(f'#{i + 1}', width=80)

        for i in columns:
            self.display_table.heading(i, text=i, anchor='w')

        self.display_table.column('#0', width=0, stretch=NO)
        self.display_table.heading('#0', text='', anchor=CENTER)
        for i, j in enumerate(self.result_table):
            self.display_table.insert(parent='', index=i, values=j)

        for j in self.result_table:
            del j[0]