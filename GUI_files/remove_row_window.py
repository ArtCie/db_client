from tkinter import *
from tkinter import ttk
from copy import deepcopy

from GUI_files.template import Template
from tkinter import messagebox
from Logic import Row
from Logic.Table import Table
from Logic.Column import Column


class RemoveRowWindow(Template):
    def __init__(self, master, active_table, parent):
        Template.__init__(self, master, active_table, parent, "800x500+200+200")
        self.display_table = ttk.Treeview(self.master, selectmode='extended')
        self.display_table.place(x=20, y=20)

        self.remove_data = ttk.Treeview(self.master, selectmode='extended')
        self.remove_data.place(x=400, y=20)

        self.button_right = Button(master)
        self.button_left = Button(master)

        self.widgets()
        master.mainloop()

    def widgets(self):
        Template.display_table(self.display_table, self.active_table)
        table = Table("remove")
        for i in zip(self.active_table.get_column_types(), self.active_table.get_column_names()):
            table.add_column(Column(str(i[0]), i[1]))
        Template.display_table(self.remove_data, table)

        self.button_right.config(text="=>", width=4, height=2, command=lambda: self.move(self.remove_data, self.display_table))
        self.button_right.place(x=310, y=80)
        self.button_left.config(text="<=", width=4, height=2, command=lambda: self.move(self.display_table, self.remove_data))
        self.button_left.place(x=310, y=150)

    def add(self):
        try:
            self.active_table.add_row(Row.Row([obj.get() for obj in self.enter_values]))
            self.parent.display_content()
            self.master.withdraw()
        except ValueError:
            messagebox.showerror("Error", "Unable to cast")

    @staticmethod
    def move(table_in, table_out):
        selection = table_out.selection()
        index = 0
        for i in selection:
            item = table_out.item(i)
            if table_in.get_children():
                for ind, child in enumerate(table_in.get_children()):
                    temp_item = table_in.item(child)
                    print(int(temp_item['values'][0]), int(item['values'][0]))
                    if int(temp_item['values'][0]) < int(item['values'][0]):
                        table_in.insert(parent='', index=ind + 1, values=item['values'])
                        break
                else:
                    table_in.insert(parent='', index=0, values=item['values'])
            else:
                table_in.insert(parent='', index=index, values=item['values'])
                index += 1
            table_out.delete(i)
