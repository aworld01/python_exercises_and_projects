"""
mixer.init() #to initialize pygame (must)
mixer.music.load(path) #to load file from path

mixer.music.play() #to play (it will play by loop)
mixer.music.play(0) #to disable loop playing

mixer.music.stop() #to stop playing music
mixer.music.pause() #to pause playing music
mixer.music.unpause() #to unpause paused music

"""

from pygame import mixer
"""define a function"""
# def play(file):
#     mixer.init()
#     mixer.music.load(file)
#     while True:
#         usr_input  = input("Enter your commands: ")
#         if usr_input == "play":
#             mixer.music.play(loops=0)
#         elif usr_input == "stop":
#             mixer.music.stop()
#             break
#         elif usr_input == "pause":
#             mixer.music.pause()
#         elif usr_input == "unpause":
#             mixer.music.unpause()


from pygame import mixer
def speak(file, com="play"):
    mixer.init()
    mixer.music.load(file)
    while True:
        if com == "play":
            mixer.music.play()
            print(com)
            break
        elif com == "stop":
            mixer.music.stop()
            break

if __name__=="__main__":
    path = "../Noice.wav"
    speak(path)