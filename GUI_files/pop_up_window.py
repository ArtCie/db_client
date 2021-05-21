from tkinter import *

from db_operations import get_data, get_types, get_columns_names, parse_input, insert
from tkinter import messagebox


class PopUpWindow(Frame):
    def __init__(self, master, content, active_base, parent):
        Frame.__init__(self, master)
        self.parent = parent
        self.master = master
        self.content = content
        self.active_base = active_base
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
        types_ = get_types(self.content[self.active_base])
        columns = get_columns_names(self.content[self.active_base])
        for i in range(len(types_)):
            new_label = Label(self.master, text=f"{columns[i]}(type={types_[i]})")
            new_label.place(x=start, y=y - 20, width=120, height=20)
            new_entry = Entry(self.master)
            new_entry.place(x=start, y=y, width=120, height=20)
            start += 130
            self.enter_values.append(new_entry)
        self.button_accept.config(text="Ok", width=12, height=2, command=self.parse_input)
        self.button_accept.place(x=300, y=250)
        self.button_cancel.config(text="Cancel", width=12, height=2, command=self.master.withdraw)
        self.button_cancel.place(x=400, y=250)

    def parse_input(self):
        entered = []
        types_ = get_types(self.content[self.active_base])
        for i in self.enter_values:
            entered.append(i.get())
        result = parse_input(entered, types_)
        if result is not True:
            messagebox.showerror("Error", result)
        else:
            self.insert(types_, entered)

    def insert(self, types_, entered):
        insert(self.content, self.active_base, types_, entered)
        self.parent.display_content()
        self.master.withdraw()

