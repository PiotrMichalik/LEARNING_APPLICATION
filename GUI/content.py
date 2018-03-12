import tkinter as tk
from GUI import menubar
from GUI.METHODS import content_methods
import time

time1 = ''

class window(tk.Frame):
    def __init__(self,master):

        tk.Frame.__init__(self, master=None)

        # size and dimension
        self.master = master
        menubar.init_window(self)

        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', content_methods.toggle_geom)
        master.maxsize(1000,400)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        time_string = time.strftime('%H:%M:%S')
        self.time = tk.Label(self, text=time_string)
        self.tick()
        self.ip = tk.Label(self, text="")
        content_methods.ipv4(self)
        self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", command=content_methods.calculate)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen.
        self.time.pack(side="top", fill="x")
        self.ip.pack(side="top", fill="x")
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def tick(self):
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            self.time.config(text=time1)
        self.time.after(200, self.tick)
