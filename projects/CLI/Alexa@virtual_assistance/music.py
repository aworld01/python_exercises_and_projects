import os
from playsound import playsound
from random import choice
from speaker import speak

path="music"
src=os.listdir(path)
def play():
    speak("playing the music")
    file=choice(src)
    music=os.path.join(path, file)
    playsound(music)
if __name__ == "__main__":
    query="play music alexa"
    if "play music" in query:
        play()