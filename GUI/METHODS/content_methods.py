import urllib.parse
import urllib.request
import re
import tkinter as tk
from tkinter.filedialog import askdirectory
from YOUTUBE_PLAYLIST_DOWNLOADER_from_console import yt_playlist_downloader as youtube_module
from GUI import content

time1 = ''


class HTML:
    """Class contained web processing"""

    def ipv4(self):
        url = 'http://ip4.me/'
        resp = urllib.request.urlopen(url)
        respData = resp.read()
        paragraphs = re.findall(
            r'((>[1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]).([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]).([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-5][0-5]).([1][0-9][0-9]|[2][0-5][0-5]|[1-9][0-9]|[1-9]|$<))',
            str(respData))
        print(paragraphs)
        self.ip.config(text="Public IP: " + paragraphs[0][0])


class Calculations:
    """Class which will cover Maths calculations"""

    def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = int(self.entry.get())
            print(i)
            result = "%s*2=%s" % (i, i * 2)
        except ValueError:
            result = "Please enter digits only"

        # set the output widget to have our result
        print(result)
        self.output.config(text=result)


class WindowFrameMethods:
    """Class which will do Window Frame changes"""

    def toggle_geom(self):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


class Youtube:
    """Class which will do Youtube operations"""

    def choose_directory_after_image_click(self):
        """"This function ask user for choose directory where music will be downloaded"""

        print("Image clicked")
        directory_name = askdirectory(title="Choose a directory.")

        if directory_name == "":
            print("None")
        else:
            print("Directory: "+directory_name)
            NewWindow(directory_name)


class NewWindow(Youtube):
    """Class which will ask about new information for Youtube Playlist download"""

    def __init__(self, directory_name):
        """Open new window for playlist insert after user chose directory"""
        self.window = tk.Tk()
        self.window.wm_title("Insert some info")

        self.playlist_window_content = tk.Label(self.window, text="Insert playlist")
        self.playlist_window_content.entry_playlist = tk.Entry(self.window)
        self.playlist_window_content.any = tk.Label(self.window, text="Insert any")
        self.playlist_window_content.entry2 = tk.Entry(self.window)
        self.playlist_window_content.submit = \
            tk.Button(self.window, text="Submit",
                      command=lambda: NewWindow.set_values_from_window(self, self.playlist_window_content.entry_playlist.get(), directory_name))
        self.playlist_window_content.output = tk.Text(self.window)

        self.playlist_window_content.grid(row=1, column=1, padx=20, pady=20)
        self.playlist_window_content.entry_playlist.grid(row=1, column=2, padx=20, pady=20)
        self.playlist_window_content.any.grid(row=2, column=1, padx=20, pady=20)
        self.playlist_window_content.entry2.grid(row=2, column=2, padx=20, pady=20)
        self.playlist_window_content.submit.grid(row=3, column=2)
        self.playlist_window_content.output.grid(row=4, column=1, rowspan=10, columnspan=5)

    def set_values_from_window(self, playlist_url, directory_name):
        """Set main values for download playlist"""
        try:
            youtube_module.playlist_url = playlist_url
            youtube_module.music_destination_folder = directory_name
            if(youtube_module.playlist_url != '') and (youtube_module.music_destination_folder != ''):
                #youtube_module.run(self)
                yt = youtube_module.YoutubePlaylistModule(playlist_url, directory_name)
                video_urls = yt.get_playlist_links_and_download_all()

        except ValueError:
            print("nic")