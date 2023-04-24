import moviepy.editor as mp #pip install moviepy

"""to convert video into audio"""
file = "test.mp4"
def audioConverter(path):
    video_path = "text.mp4"
    audio_path = "test.mp3"
    load = mp.VideoFileClip(video_path)
    load.audio.write_audiofile(audio_path)