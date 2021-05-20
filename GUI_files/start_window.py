from tkinter import *
from tkinter import filedialog
import os
from db_operations import establish_connection
from GUI_files import main_window

class StartWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.menubar = Menu(master)
        master['background'] = '#202020'
        master.geometry("600x600")
        master.title("ArthonDB Client")
        self.run(master)

    def widgets(self, master):
        load = PhotoImage(file="source/cover.png")
        panel = Label(master, image=load, borderwidth=0, highlightthickness=0)
        panel.image = load
        panel.place(x=100, y=20)

        create_database = Button(master, text="Create new database", height=2, width=20,
                                 bg='#453d49',
                                 fg='#ffffff',
                                 relief='sunken',
                                 activebackground='#4f2b64',
                                 activeforeground='#ffffff')
        open_database = Button(master, text="Open database", height=2, width=20,
                               bg='#453d49',
                               fg='#ffffff',
                               relief='sunken',
                               activebackground='#4f2b64',
                               activeforeground='#ffffff',
                               command=lambda: self.browse_files(master) )
        create_database.place(x=100, y=450)
        open_database.place(x=350, y=450)

    def browse_files(self, master):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title=r"Select a \".json\" extension file",
                                              filetypes=[("Json file", "*.json")])
        content = establish_connection(filename)
        self.switch_windows(master, content)

    @staticmethod
    def switch_windows(master, content):
        master.withdraw()
        root2 = Toplevel()
        app2 = main_window.MainWindow(root2, content)

    def run(self, master):
        master.config(menu=self.menubar)
        self.widgets(master)
        master.mainloop()

