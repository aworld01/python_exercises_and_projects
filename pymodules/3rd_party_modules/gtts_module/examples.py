
from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound
import os

"""very simple"""
def saveAudio(txt):
   tts = gTTS(text=txt) #creating instance
#    fileName = f"audios/{txt}.mp3" #file naming
   fileName = f"audios/{txt}.mp3".lower() #change fileName into lowercase
   tts.save(fileName) #save file
# saveAudio(strEng) #calling function


"""basic usecase(English)"""
def speak(txt):
    tts = gTTS(text=txt)
    """making directory if not exist"""
    if not os.path.exists("audios"):
        os.mkdir("audios")
        
    fileName = f"audios/{txt}.mp3".lower() #file naming
    tts.save(fileName)
    playsound(fileName) #playing file
# speak(strEng) #calling function


"""basic usecase(Hindi)"""
def speak(txt):
    tts = gTTS(text=txt, lang='hi')
    """making directory if not exist"""
    if not os.path.exists("audios"):
        os.mkdir("audios")
    fileName = f"audios/{txt}.mp3"
    tts.save(fileName)
    playsound(fileName)
# speak(strHin) #calling function


"""daily usecase(English)"""
def speak(txt):
    tts = gTTS(text=txt)
    if not os.path.exists("audios"):
        os.mkdir("audios")
    fileName = f"audios/{txt}.mp3".lower()
    if os.path.exists(fileName):
       playsound(fileName)
    else:
       tts.save(fileName)
       playsound(fileName)
# speak(strEng) #calling function


"""daily usecase(Hindi)"""
def speak(txt):
    tts = gTTS(text=txt, lang="hi")
    if not os.path.exists("audios"):
        os.mkdir("audios")
    fileName = f"audios/{txt}.mp3"
    if os.path.exists(fileName):
       playsound(fileName)
    else:
       tts.save(fileName)
       playsound(fileName)
# speak(strHin) #calling function


"""Final"""
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