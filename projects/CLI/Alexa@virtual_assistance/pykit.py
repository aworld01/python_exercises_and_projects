"""pip install pywhatkit"""
import pywhatkit as pykit
import webbrowser as web
from speaker2 import speak
from listener import listen

def search(query):
    speak("OK sir, this is what I found for your Search")
    query=query.replace("alexa","")
    query=query.replace("google search","")
    pykit.search(query)
    speak("Done sir")

def whatsapp(query):
    speak("tell me the name of the person")
    name=listen()
    from datetime import datetime
    time=datetime.now()
    hour=time.hour
    minute=time.minute
    if "roshan tara" in name:
        speak("tell me the message")
        msg=listen()
        pykit.sendwhatmsg_instantly("+918797217771", msg, hour, minute, 20)
        speak("the message has been sent")

def youtubePlay(query):
    query=query.replace("alexa", "")
    query=query.replace("youtube play","")
    result="https://www.youtube.com/results?search_query="+query
    speak("playing the song")
    pykit.playonyt(result)

if __name__ == "__main__":
    # search("what is the age of salman khan")

    # data="send whatsapp message"
    # if "send whatsapp" in data:
    #     whatsapp(data)

    youtubePlay("hindi new song")