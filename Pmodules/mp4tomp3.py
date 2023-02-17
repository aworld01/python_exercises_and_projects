import moviepy.editor as mp

video_path = "text.mp4"
audio_path = "test.mp3"
load = mp.VideoFileClip(video_path)
load.audio.write_audiofile(audio_path)