import urllib.parse
import urllib.request
import re
import tkinter as tk
from tkinter.filedialog import askdirectory
from YOUTUBE_PLAYLIST_DOWNLOADER_from_console import yt_playlist_downloader as youtube_module

time1 = ''



def ipv4(self):
    url = 'http://ip4.me/'
    resp = urllib.request.urlopen(url)
    respData = resp.read()
    paragraphs = re.findall(
        r'((>[1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]).([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]).([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]).([1][0-9][0-9]|[2][0-5][0-5]|[1-9][0-9]|[1-9]|$<))',
        str(respData))
    print(paragraphs)
    self.ip.config(text="Public IP: " + paragraphs[0][0])


def calculate(self):
    # get the value from the input widget, convert
    # it to an int, and do a calculation
    print(self.entry)
    try:
        i = int(self.entry.get())
        result = "%s*2=%s" % (i, i * 2)
    except ValueError:
        result = "Please enter digits only"

    # set the output widget to have our result
    self.output.configure(text=result)


def toggle_geom(self):
    geom = self.master.winfo_geometry()
    print(geom, self._geom)
    self.master.geometry(self._geom)
    self._geom = geom


def on_click(self):
    print("Image clicked")
    directory_name = askdirectory(title="Choose a directory.")

    if directory_name == "":
        print("None")
    else:
        print("Directory: "+directory_name)
        new_window(self,directory_name)


def new_window(self,directory_name):
    self.t = tk.Tk()
    self.t.wm_title("Insert some info")
    self.l = tk.Label(self.t, text="Insert playlist")
    self.l.entry_playlist = tk.Entry(self.t)

    self.l.any = tk.Label(self.t, text="Insert any")
    self.l.entry2 = tk.Entry(self.t)
    self.l.submit = tk.Button(self.t, text="Submit", command=lambda: set_values_from_window(self, self.l.entry_playlist.get(), directory_name))
    self.l.output = tk.Text(self.t)


    self.l.grid(row=1, column=1, padx=20, pady=20)
    self.l.entry_playlist.grid(row=1, column=2, padx=20, pady=20)
    self.l.any.grid(row=2, column=1, padx=20, pady=20)
    self.l.entry2.grid(row=2, column=2, padx=20, pady=20)
    self.l.submit.grid(row=3, column=2)
    self.l.output.grid(row=4, column=1, rowspan=10, columnspan=5)


def set_values_from_window(self, playlist_url, directory_name):
    print("#TUTAJ")

    try:
        print(playlist_url)
        print(directory_name)
        youtube_module.playlist_url = playlist_url
        youtube_module.music_destination_folder = directory_name
        if(youtube_module.playlist_url != '') and (youtube_module.music_destination_folder != ''):
            youtube_module.run(self)
    except ValueError:
        print("nic")