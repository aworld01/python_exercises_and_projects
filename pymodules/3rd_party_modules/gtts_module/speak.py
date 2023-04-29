import os
from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound

def speak(txt, fileName="default"):
    tts = gTTS(text=txt, lang="hi")

    """make directory if not exist"""
    if not os.path.exists("audios"):
        os.mkdir("audios")

    """file naming"""
    if fileName == "default":
        fileName = f"audios/{txt}.mp3".lower()
    else:
        fileName = f"audios/{fileName}.mp3".lower()

    """checking file exists if not then save"""
    if os.path.exists(fileName):
        playsound(fileName)
    else:
        tts.save(fileName)
        playsound(fileName)
       
if(__name__=='__main__'):
   strEng = "HEllo world how are you"
   strHin = "नमस्ते दुनिया वालों आप कैसे हो"

   speak(strEng) #example1 (strEng as a data)
#    speak(strHin) #example2 (strHin as a data)
#    speak(strHin,strEng) #example3 (strHin as a data, strEng as a fileName)
#    speak(strEng,strHin) #example4 (strEng as a data, strHin as a fileName)