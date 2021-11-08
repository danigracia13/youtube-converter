from pytube import YouTube, Playlist

def processUrlMP4():
    url_input = "https://www.youtube.com/watch?v=QF08nvtHHCY"
    yt = YouTube(url_input)
    file_name=(yt.title + ".mp4")
    stream = yt.streams.get_highest_resolution()
    stream.download("./download")

    return file_name

processUrlMP4()