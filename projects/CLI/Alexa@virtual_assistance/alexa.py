import os
import pykit
import web
from music import play
from listener import listen
from speaker import speak
from wish_me import wishMe
from wiki import wiki
from trans import tran
from temperature import temp
from netSpeed import speedTest
from getTime import Time
from battary import batt

wishMe()

while True:
    query=listen()
    if "how are you" in query:
        speak("I'm fine sir")
    elif "who are you" in query:
        speak("I'm a computer program my name is alexa")
    elif "what is your name" in query:
        speak("My name is alexa, you can call me computer sir")
    elif "how old are you" in query:
        speak("I'm 18 years old now sir")
    elif "where are you from" in query:
        speak("I'm from India sir")
    elif "who is your boss" in query:
        speak("Abdul Zoha sir is my boss")
    elif "i love you" in query:
        speak("It's my luck that you love me sir, I love you too")
    elif "will you marry me" in query:
        speak("I'm a computer program so how can i marry you sir")
    
    elif "wikipedia" in query:
        wiki(query)
    elif "google search" in query:
        pykit.search(query)
    elif "send whatsapp" in query:
        pykit.whatsapp(query)
    elif "youtube play" in query:
        pykit.youtubePlay(query)
    elif "open website" in query:
        web.go(query)
    elif "check aadhar" in query:
        web.aadhaar()
    elif "check pan" in query:
        web.pan()
    elif "youtube search" in query:
        web.youtubeSearch(query)
    elif "open translator" in query:
        tran()
    elif "tell me the temperature" in query:
        temp()
    elif "play music" in query:
        play()
    elif "check net speed" in query:
        speedTest()
    elif "open chromium" in query:
        os.system("/usr/bin/chromium %U")
    elif "tell me the time" in query:
        Time()
    elif "what is the time" in query:
        Time()
    elif "show me the battery" in query:
        batt()


    elif "restart" in query:
        speak("The system is going to be restart")
        os.system("python3 alexa.py")
    elif "clear the terminal" in query:
        speak("OK sir, I am clear the terminal")
        os.system("clear")
    elif "you need a break" in query:
        speak("ok sir, you can call me anytime")
        os.system("clear")
        break 
    elif "goodbye" in query:
        speak("shuting down, goodbye sir")
        os.system("shutdown now")