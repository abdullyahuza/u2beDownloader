import pytube

def downloadVideo(url, resolution):
    itag = chooseResolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def downloadVideos(urls, resolution):
    for url in urls:
        downloadVideo(url, resolution)

def downloadPlaylist(url, resolution):
    playlist = pytube.Playlist(url)
    downloadVideos(playlist.video_urls, resolution)

def chooseResolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag

def inputLink():
    print("Enter the link of the video:")
    link = input()

    return link

def inputLinks():
    print("Enter the links of the videos (end by entering 'END'):")

    links = []
    link = ""

    while link != "END" and link != "end":
        link = input()
        links.append(link)

    links.pop()

    return links