#!/usr/bin/env python
import os, sys, time
import argparse
import tkinter as tk
from urllib.request import *
from GUI.METHODS import content_methods

import pytube  # pip install pytube

temp = "https://www.youtube.com/playlist?list=PLkufxprtg8Qkb-xzwe4vMbamCqaQFEF7c&disable_polymer=true"

class YoutubePlaylistModule:
    """Youtube module which download playlist after specify
    Playlist url and destination folder where it should be downloaded"""

    def __init__(self, playlist_url, music_destination_folder):
        """Set variables to object names"""
        self.playlist_url = playlist_url
        self.music_destination_folder = music_destination_folder
        print(playlist_url)
        print(music_destination_folder)

    def _start_download(self, video_urls):
        iteration = 1
        max_iterations = len(video_urls)
        #self.output.insert(1.0, "sample text")
        for u in video_urls:
            u = u.decode()
            yt = pytube.YouTube(u)
            vid = yt.streams.filter(only_audio=True).first()

            print('Downloading {}/{}'.format(iteration, max_iterations))
            iteration = iteration + 1
            vid.download(self.music_destination_folder)

    def _confirmation_window_command(self, video_urls, value):
        confirmation = value
        self.confirmation_window.destroy()
        if confirmation in ['y']:
            YoutubePlaylistModule._start_download(self, video_urls)

    def get_playlist_links_and_download_all(self):
        """Get music files from playlist url"""
        page_elements = urlopen(self.playlist_url).readlines()
        video_elements = [el for el in page_elements if b'pl-video-title-link' in el]  # Filter out unnecessary lines
        video_urls = [v.split(b'href="', 1)[1].split(b'" ', 1)[0] for v in video_elements]  # Grab the video urls from the elements

        self.confirmation_window = tk.Tk()
        self.confirmation_window.wm_title("Agree?")

        confirmation_window_label = tk.Label(
            self.confirmation_window, text=
            'You are about to download {} videos to {}\n'
            'Would you like to continue? '.format(len(video_urls), self.music_destination_folder))

        confirmation_window_button_yes = \
            tk.Button(self.confirmation_window, text="YES",
                      command=lambda: YoutubePlaylistModule._confirmation_window_command(self, video_urls, "y"))

        confirmation_window_button_no = \
            tk.Button(self.confirmation_window,text="NO",
                      command=lambda: YoutubePlaylistModule._confirmation_window_command(self, video_urls, "n"))

        confirmation_window_label.grid(row=1, column=1, columnspan=6, padx=20, pady=20)
        confirmation_window_button_no.grid(row=2, column=2, columnspan=2, padx=20, pady=20)
        confirmation_window_button_yes.grid(row=2, column=4, columnspan=2, padx=20, pady=20)

        return [b'http://www.youtube.com' + v for v in video_urls]
