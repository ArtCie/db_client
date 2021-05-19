from tkinter import *
from tkinter import filedialog
import os

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.menubar = Menu(self.root)
        self.root['background'] = '#202020'
        self.root.geometry("600x600")
        self.root.title("ArthonDB Client")
        self.run()

    def widgets(self):
        load = PhotoImage(file="source/cover.png")
        panel = Label(self.root, image=load, borderwidth=0, highlightthickness=0)
        panel.image = load
        panel.place(x=100, y=20)

        create_database = Button(self.root, text="Create new database", height=2, width=20,
                                 bg='#453d49',
                                 fg='#ffffff',
                                 relief='sunken',
                                 activebackground='#4f2b64',
                                 activeforeground='#ffffff')
        open_database = Button(self.root, text="Open database", height=2, width=20,
                               bg='#453d49',
                               fg='#ffffff',
                               relief='sunken',
                               activebackground='#4f2b64',
                               activeforeground='#ffffff',
                               command=self.browseFiles)
        create_database.place(x=100, y=450)
        open_database.place(x=350, y=450)

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title=r"Select a \".json\" extension file",
                                              filetypes=[("Json file", "*.json")])
        print(filename)

    def run(self):
        self.root.config(menu=self.menubar)
        self.widgets()
        self.root.mainloop()


def main():
    root = MainWindow()


if __name__ == '__main__':
    main()
