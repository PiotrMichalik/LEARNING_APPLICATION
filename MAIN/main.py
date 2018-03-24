import tkinter as tk
from GUI import content


# if this is run as sa program (versus being imported),
# create a root window and asn sinstance of our example,
# then start the event loop

if __name__ == "__main__":

    root = tk.Tk()
    content.Window(root).pack(fill="both", expand=True)
    root.mainloop()
    ## GIT
