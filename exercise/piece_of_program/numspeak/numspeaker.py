from playsound import playsound

def sounder(arg):
    for sound in arg:
        if sound == "1":
            playsound("audios/one.mp3")
        elif sound == "2":
            playsound("audios/two.mp3")
        elif sound == "3":
            playsound("audios/three.mp3")
        elif sound == "4":
            playsound("audios/four.mp3")
        elif sound == "5":
            playsound("audios/five.mp3")
        elif sound == "6":
            playsound("audios/six.mp3")
        elif sound == "7":
            playsound("audios/seven.mp3")
        elif sound == "8":
            playsound("audios/eight.mp3")
        elif sound == "9":
            playsound("audios/nine.mp3")
        elif sound == "0":
            playsound("audios/zero.mp3")

if __name__=="__main__":
    usr = input("Please Enter Your Number: ")
    sounder(usr)