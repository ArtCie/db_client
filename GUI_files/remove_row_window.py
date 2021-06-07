from tkinter import *
from tkinter import ttk

from GUI_files.template import Template
from tkinter import messagebox
from Logic.Table import Table
from Logic.Column import Column


class RemoveRowWindow(Template):
    """Class represents remove row window"""
    def __init__(self, master, active_table, parent):
        """Constructor defines window objects"""
        Template.__init__(self, master, active_table, parent, "670x500+200+200")

        self.master.title("Remove row")

        self.display_table = ttk.Treeview(self.master, selectmode='extended')
        self.display_table.place(x=20, y=20)

        self.remove_data = ttk.Treeview(self.master, selectmode='extended')
        self.remove_data.place(x=400, y=20)

        self.button_right = Button(master)
        self.button_left = Button(master)

        self.button_accept = Button(master)
        self.button_cancel = Button(master)

        self.widgets()
        master.mainloop()

    def widgets(self):
        """Adjust details of widgets"""
        Template.display_table(self.display_table, self.active_table)
        table = Table("remove")
        for i in zip(self.active_table.get_column_types(), self.active_table.get_column_names()):
            table.add_column(Column(str(i[0]), i[1]))
        Template.display_table(self.remove_data, table)

        self.button_right.config(text="=>", width=4, height=2,
                                 command=lambda: self.move(self.remove_data, self.display_table))
        self.button_right.place(x=310, y=80)
        self.button_left.config(text="<=", width=4, height=2,
                                command=lambda: self.move(self.display_table, self.remove_data))
        self.button_left.place(x=310, y=150)

        self.button_accept.config(text="Delete", width=15, height=2, command=self.accept_window)
        self.button_accept.place(x=390, y=400)
        self.button_cancel.config(text="Cancel", width=15, height=2, command=self.master.withdraw)
        self.button_cancel.place(x=520, y=400)

    def accept_window(self):
        """Method calls window to ask user if he is certain to remove rows"""
        msg_box = messagebox.askquestion('Delete rows', 'Are you sure you want to delete these rows?', icon='warning')
        if msg_box == 'yes':
            self.remove()

    def remove(self):
        """Method removes chosen rows"""
        for i in self.remove_data.get_children():
            item = self.remove_data.item(i)['values'][1:]
            remove_item = self.active_table.get_obj(item)
            self.active_table.remove_row(remove_item)
        self.parent.display_content()
        self.master.withdraw()

    @staticmethod
    def move(table_in, table_out):
        """Method moves from one ttk.Treview to another"""
        selection = table_out.selection()
        index = 0
        for i in selection:
            item = table_out.item(i)
            if table_in.get_children():
                for ind, child in enumerate(table_in.get_children()):
                    temp_item = table_in.item(child)
                    if int(temp_item['values'][0]) < int(item['values'][0]):
                        table_in.insert(parent='', index=ind + 1, values=item['values'])
                        break
                else:
                    table_in.insert(parent='', index=0, values=item['values'])
            else:
                table_in.insert(parent='', index=index, values=item['values'])
                index += 1
            table_out.delete(i)
