from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound
import os

"""basic code(Hindi)"""
# def speak(txt):
#     if not os.path.exists("audios"):
#         os.mkdir("audios")
#     tts = gTTS(text=txt, lang='hi')
#     fileName = f"audios/{txt}.mp3"
#     tts.save(fileName)
#     playsound(fileName)
       
# data='मेरा नाम एलेक्सा है'
# speak(data)




"""basic code(English)"""
# def speak(txt):
#     if not os.path.exists("audios"):
#         os.mkdir("audios")
#     data=txt.lower()
#     tts = gTTS(text=data, lang='en-in')
#     fileName = f"audios/{data}.mp3"
#     tts.save(fileName)
#     playsound(fileName)
       
# data='My NAMe Is cortana'
# speak(data)




"""Final"""
def speak(txt):
    if not os.path.exists("audios"):
        os.mkdir("audios")
    data = txt.lower()
    tts = gTTS(text=data, lang='en-in')
    fileName = f"audios/{data}.mp3"
    if os.path.exists(fileName):
       playsound(fileName)
    else:
       tts.save(fileName)
       playsound(fileName)
       
if(__name__=='__main__'):
   data='My NAMe Is AleXa'
   speak(data)