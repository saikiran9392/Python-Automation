from pytube import YouTube
url = "https://youtu.be/0CPIN9LOdyo?si=5iB-gDJiMjhMgdMt"
file = YouTube(url)
def get_resolution(s):
    return int(s.resolution[:-1])
stream = max(
    filter(lambda s: get_resolution(s) <= 1080,  # filter out sub-1080p streams
           filter(lambda s: s.type == 'video', file.fmt_streams)), # filter out the video streams
    key=get_resolution  # maximum resolution among those streams
)
print(stream)
stream.download('file.mp4')
