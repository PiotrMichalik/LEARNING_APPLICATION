import urllib.parse
import urllib.request
import re
from tkinter.filedialog import askdirectory
import YOUTUBE_PLAYLIST_DOWNLOADER_from_console as youtube_module

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
