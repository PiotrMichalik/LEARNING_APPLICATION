import tkinter as tk
from tkinter import ttk
import os

from GUI import menubar
from GUI.METHODS import content_methods
from PIL import Image, ImageTk
import time

path_images="\GUI\Images\\"
youtube_image_name="Youtube.jpg"
download_music_to_folder="D:\Muzyka"
time1 = ''


class Window(tk.Frame):
    def __init__(self,master):

        tk.Frame.__init__(self, master=None)

        # size and dimension
        self.master = master
        menubar.init_window(self)

        pad = 3
        self._geom = '700x700+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', content_methods.WindowFrameMethods.toggle_geom(self))
        master.maxsize(1000, 400)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        time_string = time.strftime('%H:%M:%S')
        self.time = tk.Label(self, text=time_string)
        self.tick()
        self.ip = tk.Label(self, text="")
        content_methods.HTML.ipv4(self)
        self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
        self.entry = tk.Entry(self)
        self.output = tk.Label(self, text="")
        self.submit = tk.Button(self, text="Submit", command=lambda: content_methods.Calculations.calculate(self))


        # Youtube
        path_program = os.path.dirname(os.getcwd())
        yt_img = ImageTk.PhotoImage(Image.open(path_program+path_images+youtube_image_name))

        self.YT_img = tk.Label(self, image=yt_img)
        self.YT_img.image = yt_img

        # excel
        self.tree = ttk.Treeview(self)

        self.tree["columns"] = ("one", "two")
        self.tree.column("one", width=100)
        self.tree.column("two", width=100)
        self.tree.heading("one", text="coulmn A")
        self.tree.heading("two", text="column B")

        self.tree.insert("", 0, text="Line 1", values=("1A", "1b"))

        id2 = self.tree.insert("", 1, "dir2", text="Dir 2")
        self.tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))

        # alternatively:
        self.tree.insert("", 3, "dir3", text="Dir 3")
        self.tree.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))

        # lay the widgets out on the screen.
        self.time.grid(row=1, column=1, padx=0, pady=0)
        self.ip.grid(row=1, column=5, padx=0, pady=0)
        self.prompt.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        self.entry.grid(row=2, column=3, columnspan=1, padx=10, pady=10)
        self.output.grid(row=2, column=4, columnspan=1, padx=10, pady=10)
        self.submit.grid(row=2, column=5, columnspan=1, padx=10, pady=10)
        self.YT_img.grid(row=4, column=1, columnspan=1, padx=10, pady=10)
        self.tree.grid(row=6, column=2, columnspan=4, rowspan=4, padx=10, pady=10)

        # clickable youtube image
        self.YT_img.bind('<Button-1>', content_methods.Youtube.choose_directory_after_image_click)

       # self.scrollbar = tk.Scrollbar(self.tree)
       # self.scrollbar.pack(side="right", fill="y")
       # self.tree.config(yscrollcommand=self.scrollbar.set)
       # self.scrollbar.config(command=self.tree.yview)

    def tick(self):
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            self.time.config(text=time1)
        self.time.after(200, self.tick)

