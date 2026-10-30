from googletrans import Translator
from listener_hindi import listen
from speaker2 import speak

def tran():
    speak("tell me the line")
    line=listen()
    translate=Translator()
    result=translate.translate(line)
    text=result.text
    speak("The Translation for this line is:"+text)