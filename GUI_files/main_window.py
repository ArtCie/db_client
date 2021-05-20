from tkinter import *
from db_operations import get_tables


class MainWindow(Frame):
    def __init__(self, master, content):
        Frame.__init__(self, master)
        master.geometry("1000x1200+000+000")
        master['background'] = '#202020'
        self.widgets(master, content)

    def widgets(self, master, content):
        tables = get_tables(content)
        self.display_tables(master, tables)

    def display_tables(self, master, tables):
        display_label = LabelFrame(master, text="siema", width=100, height=1030, bg="#493358", fg="#ffffff", bd=0)
        display_label.config(font=("Arial", 10))
        display_label.place(x=0, y=20)
        for table in tables:
            button = Button(display_label, text=table, width=100, bg='#453d49',
                            fg='#ffffff', relief='sunken', activebackground='#4f2b64',
                            activeforeground='#ffffff')
            button.pack()
        display_label.pack_propagate(0)
