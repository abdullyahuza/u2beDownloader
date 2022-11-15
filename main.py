print("Welcome to u2be \nA YouTube Downloader and Converter v0.1")
print("Loading...")

import pytube
import u2beDownloader
import fileConverter

print('''
What do you want?

(1) Download a Video
(2) Download a Playlist
(3) Download Video and Convert Into MP3

Copyright (c) Abdull Yahuza 2022
''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "1":
        link = u2beDownloader.inputLink()
        u2beDownloader.downloadVideo(link, quality)
        print("Download finished!")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        u2beDownloader.downloadPlaylist(link, quality)
        print("Download finished!")
elif choice == "3":
    link = u2beDownloader.inputLink()
    print("Downloading...")
    filename = u2beDownloader.downloadVideo(link, 'low')
    print("Converting...")
    fileConverter.convertToMP3(filename)
else:
    print("Invalid input! Terminating...")
