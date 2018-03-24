#!/usr/bin/env python
import os, sys, time
import argparse
import tkinter as tk
from urllib.request import *

import pytube  # pip install pytube

playlist_url = ''
confirmation = ''
music_destination_folder = ''
temp = "https://www.youtube.com/playlist?list=PLkufxprtg8Qkb-xzwe4vMbamCqaQFEF7c&disable_polymer=true"


def run(self):

    print("!!playlist; ")
    print(playlist_url)
    print("!!Music_destination_folder: ")
    print(music_destination_folder)

    def get_playlist_links(playlist_url):
        ### PROXY - https://stackoverflow.com/questions/5620263/using-an-http-proxy-python
        # proxy_support = ProxyHandler({"http": "10.156.237.254:8080"})
        # opener = build_opener(proxy_support)
        # install_opener(opener)

        page_elements = urlopen(playlist_url).readlines()

        video_elements = [el for el in page_elements if b'pl-video-title-link' in el]  # Filter out unnecessary lines
        video_urls = [v.split(b'href="', 1)[1].split(b'" ', 1)[0] for v in video_elements]  # Grab the video urls from the elements
        return [b'http://www.youtube.com' + v for v in video_urls]


    parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-p PLAYLISTURL] [-d DESTINATION]')
    parser.add_argument('-p', '--playlisturl', help='url of the playlist to be downloaded', default=playlist_url, metavar='')
    parser.add_argument('-d', '--destination', help='path of directory to save videos to', default=music_destination_folder, metavar='')
    args = parser.parse_args()


    if os.path.exists(args.destination):
        directory_contents = [f.split('.mp4', 1)[0] for f in os.listdir(args.destination) if f.endswith('.mp4')]
    else:
        print('Destination directory does not exist')
        sys.exit(1)

    video_urls = get_playlist_links(args.playlisturl)

    self.confirmation_window = tk.Tk()
    self.confirmation_window.wm_title("Agree?")
    self.confirmation_window_label = tk.Label(
        self.confirmation_window, text='You are about to download {} videos to {}\nWould you like to continue? '
            .format(len(video_urls), music_destination_folder))

    def start_download(self):
        iteration = 1
        max_iterations = len(video_urls)
        #self.output.insert(1.0, "sample text")
        for u in video_urls:
            u = u.decode()
            yt = pytube.YouTube(u)
            vid = yt.streams.filter(only_audio=True).first()

            print('Downloading {}/{}'.format(iteration, max_iterations))
            iteration = iteration + 1
            vid.download(args.destination)

    def confirmation_window_command(self,value):
        confirmation = value
        self.confirmation_window.destroy()
        if confirmation in ['y']:
            start_download(self)

    self.confirmation_window_button_yes = tk.Button(self.confirmation_window,
                                                    text="YES", command=lambda: confirmation_window_command(self, "y"))
    self.confirmation_window_button_no = tk.Button(self.confirmation_window,
                                                   text="NO", command=lambda: confirmation_window_command(self, "n"))

    self.confirmation_window_label.grid(row=1, column=1, columnspan=6, padx=20, pady=20)
    self.confirmation_window_button_no.grid(row=2, column=2, columnspan=2, padx=20, pady=20)
    self.confirmation_window_button_yes.grid(row=2, column=4, columnspan=2, padx=20, pady=20)


    print('Done')
