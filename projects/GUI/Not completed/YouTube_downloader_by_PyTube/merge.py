import moviepy.editor as mpe #import package

"""example1"""
# clip = mpe.VideoFileClip("videos/song.mp4") #to add video to path
# bg_audio = mpe.AudioFileClip("audios/audio.mp4") #to add bg_audio to path
# audio = mpe.CompositeAudioClip([bg_audio, clip.audio])
# final = clip.set_audio(audio) #to set audio into video file
# final.write_videofile("mixed.mp4") #to create a new file

"""example2"""
clip = mpe.VideoFileClip("videos/video.mp4") #to add video to path
audio = mpe.AudioFileClip("audios/audio.mp4") #to add audio to path
final = clip.set_audio(audio) #to set audio into video file
final.write_videofile("mixed.mp4") #to create a new file