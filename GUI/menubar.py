import tkinter as tk

def init_window(self):
    # changing the title of our master widget
    self.master.title("GUI")

    # allowing the widget to take the full space of the root window
    self.pack(fill='x', expand=1)

    # creating a menu instance
    menu = tk.Menu(self.master)
    self.master.config(menu=menu)

    # create the file object)
    file = tk.Menu(menu)

    # adds a command to the menu option, calling it exit, and the
    # command it runs on event is client_exit
    file.add_command(label="Exit", command=client_exit, activebackground='Gray', activeforeground='Red')
    file.add_command(label="New", command=donothing)
    file.add_command(label="Open", command=donothing)
    file.add_command(label="Save", command=donothing)
    file.add_command(label="Save as...", command=donothing)
    file.add_command(label="Close", command=donothing)
    # added "file" to our menu
    menu.add_cascade(label="File", menu=file)

    # create the file object)
    edit = tk.Menu(menu)

    # adds a command to the menu option, calling it exit, and the
    # command it runs on event is client_exit
    edit.add_command(label="Undo")

    # added "file" to our menu
    menu.add_cascade(label="Edit", menu=edit)

def client_exit():
    exit()
def donothing():
    print("Do Nothing")