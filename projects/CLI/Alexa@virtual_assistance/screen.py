# pip install pyautogui
import pyautogui as src
from speaker2 import speak
from listener import listen
import os

def src():
    speak("OK sir, what should i name that file")
    name=listen()
    file=name+".png"
    path="/home/thor/Desktop"+file
    tk=src.screenshot()
    tk.save(path)
    os.startfile(path)
    speak("here is your screenshot")
if __name__ == "__main__":
    data=src()
    if "take screenshot" in data:
        src()