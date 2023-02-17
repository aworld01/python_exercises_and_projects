##pip install requests
##pip install bs4

import requests
from bs4 import BeautifulSoup as bs
from speaker2 import speak
from listener import listen

def temp():
    speak("tell me the area")
    search=listen()
    url=f"https://www.google.com/search?client=firefox-b-e&q=temperature in {search}"
    r=requests.get(url)
    data=bs(r.text,"html.parser")
    temperature=data.find("div",class_="BNeawe").text
    print(f"The temperature outside in {search} is {temperature}")
    speak(f"The temperature outside in {search} is {temperature}")