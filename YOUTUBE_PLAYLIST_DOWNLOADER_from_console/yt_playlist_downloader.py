#!/usr/bin/env python
import os, sys, time
import argparse
from urllib.request import *

import pytube  # pip install pytube

CS294_playlist_url = "https://www.youtube.com/playlist?list=PLkufxprtg8Qkb-xzwe4vMbamCqaQFEF7c&disable_polymer=true"
Music_destination_folder = "D:\Muzyka\do_samochodu_1"
def run():
    def get_playlist_links(playlist_url):
        ### PROXY - https://stackoverflow.com/questions/5620263/using-an-http-proxy-python
        # proxy_support = ProxyHandler({"http": "10.156.237.254:8080"})
        # opener = build_opener(proxy_support)
        # install_opener(opener)

        page_elements = urlopen(playlist_url).readlines()

        video_elements = [el for el in page_elements if b'pl-video-title-link' in el]  # Filter out unnecessary lines
        video_urls = [v.split(b'href="', 1)[1].split(b'" ', 1)[0] for v in video_elements]  # Grab the video urls from the elements
        #print(video_urls)
        return [b'http://www.youtube.com' + v for v in video_urls]

    start_time = time.time()

    def print_dot(bytes_received, file_size, start):
        global start_time
        if time.time() - start_time > 1.0:
            sys.stdout.write('.')
            sys.stdout.flush()
            start_time = time.time()


    parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-p PLAYLISTURL] [-d DESTINATION]')
    parser.add_argument('-p', '--playlisturl', help='url of the playlist to be downloaded', default=CS294_playlist_url, metavar='')
    parser.add_argument('-d', '--destination', help='path of directory to save videos to', default=Music_destination_folder, metavar='')
    args = parser.parse_args()


    if os.path.exists(args.destination):
        directory_contents = [f.split('.mp4', 1)[0] for f in os.listdir(args.destination) if f.endswith('.mp4')]
    else:
        print('Destination directory does not exist')
        sys.exit(1)

    video_urls = get_playlist_links(args.playlisturl)
    #print("!!## VIDEO_URLS")
    #print(video_urls)
    confirmation = input('You are about to download {} videos to {}\nWould you like to continue? [Y/n] '.format( len(video_urls), Music_destination_folder))

    iteration=1
    max_iterations=len(video_urls)
    if confirmation.lower() in ['y', '']:
        for u in video_urls:
            #print("!!")
            #print(u)
            #print(type(u))
            u = u.decode()
            #print("!! DECODE ")
            #print(u)
            yt = pytube.YouTube(u)
            #print("??")
            #print(type(yt))
            #print("?? YT")
            #print(yt)
            vid = yt.streams.filter(only_audio=True).first()
            #vid = yt.streams.last()
            #print("@@ VID")
            #print(vid)

            print('Downloading {}/{}'.format(iteration, max_iterations))
            iteration = iteration + 1
            vid.download(args.destination)

    print('Done')
