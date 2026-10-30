import webbrowser
from speaker2 import speak
from listener import listen


def go(query):
    speak("Tell me the name of the website")
    name=listen()
    web="https://www."+name
    webbrowser.open(web)
    speak("Done sir")

def aadhaar():
    speak("OK sir, this is what I found for your Search")
    webbrowser.open("https://uidai.gov.in/")
    speak("Done sir")

def pan():
    speak("OK sir, this is what I found for your Search")
    webbrowser.open("https://tin.tin.nsdl.com/pantan/StatusTrack.html")
    speak("Done sir")

def youtubeSearch(query):
    speak("OK sir, this is what I found for your Search")
    query=query.replace("alexa", "")
    query=query.replace("youtube search","")
    web='https://www.youtube.com/results?search_query='+query
    webbrowser.open(web)
    speak("Done sir")

if __name__ == "__main__":
    go("open website")

    query="check aadhar online"
    if "check aadhar" in query:
        url()