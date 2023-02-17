"""
sudo apt install python3-pip -y #to install python3 pip
pip install pytube #to install pytube module



url = "https://www.youtube.com/watch?v=QzGZg8SPrac"

yt = YouTube(url) #to make object.

title = yt.title #to fetch title
print(title)

desc = yt.description #to fetch description
print(desc)

desc = yt.description[:100] #to fetch video description sliced in 100 words only.
print(desc)

# thumbnail = yt.thumbnail_url #to fetch thumbnail
# print(thumbnail)

st = yt.streams #to fetch all streams
# print(st)

to fetch all streams one-by-one
for stream in st:
    print(stream)

video_files = st.filter(progressive=True) #to fetch all videos including audio.
# print(video_files)

video_file = st.filter(progressive=True).first() #to fetch first video including audio.
# print(video_file)

audio_files = st.filter(type="audio") #to fetch only audio files
print(audio_files)

audio_files = st.filter(only_audio=True) #to fetch only audio files
print(audio_files)

audio_file = st.filter(type="audio").first() #to fetch first audio file.
print(audio_file)

video_file.download("./") #to download video file.
audio_file.download("./") #to download audio file.

# n = len(st) #to get lenth of streams
# print(n)

progressive=True = audio/video
adaptive=True = only video
vid = st.filter(file_extension='mp4')



url1 = "https://www.youtube.com/watch?v=QzGZg8SPrac"
url2 = "https://www.youtube.com/watch?v=bTM3vz9T-7s"
url3 = "https://www.youtube.com/watch?v=9cLInXL5OvQ"
url4 = "https://www.youtube.com/watch?v=XYY33050xfg"
url5 = "https://www.youtube.com/watch?v=6FgFXmflPQY"

"""
from pytube import* #pip install pytube

def progress_(streams, chunk, bytes_remaining):
    print(f"Streams: {streams}")
    print(f"Chunk: {chunk}")
    print(f"bytes_remaining: {bytes_remaining}")

url = "https://www.youtube.com/watch?v=YxWlaYCA8MU"

# yt = YouTube(url, on_progress_callback=progress_) #to make object.
yt = YouTube(url)

st = yt.streams #to fetch all streams

hd = st.filter(mime_type="video/mp4", res="720p", adaptive=True) #to fetch hd video

# fhd = st.filter(mime_type="video/mp4", res="1080p", adaptive=True) #to fetch full hd video

# for file in hd:
#     file.download()