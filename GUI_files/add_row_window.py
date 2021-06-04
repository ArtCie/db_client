from tkinter import *

from tkinter import messagebox
from Logic import Row


class PopUpWindow(Frame):
    def __init__(self, master, content, active_table, parent):
        Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.content = content
        self.active_table = active_table
        self.enter_values = []
        self.grid()
        self.menubar = Menu(master)
        self.button_accept = Button(master)
        self.button_cancel = Button(master)

        self.master['background'] = '#202020'
        self.master.geometry("500x300+200+200")
        self.master.title("Insert into ")

        self.widgets()
        master.mainloop()

    def widgets(self):
        start, y = 20, 40
        types_ = self.active_table.get_column_types()
        columns = self.active_table.get_column_names()
        for i in range(len(types_)):
            new_label = Label(self.master, text=f"{columns[i]}(type={types_[i].__name__})")
            new_label.place(x=start, y=y - 20, width=120, height=20)
            new_entry = Entry(self.master)
            new_entry.place(x=start, y=y, width=120, height=20)
            start += 130
            self.enter_values.append(new_entry)
        self.button_accept.config(text="Ok", width=12, height=2, command=self.add)
        self.button_accept.place(x=300, y=250)
        self.button_cancel.config(text="Cancel", width=12, height=2, command=self.master.withdraw)
        self.button_cancel.place(x=400, y=250)

    def add(self):
        try:
            self.active_table.add_row(Row.Row([obj.get() for obj in self.enter_values]))
            self.parent.display_content()
            self.master.withdraw()
        except ValueError:
            messagebox.showerror("Error", "Unable to cast")