import os
from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound

def fileSave(txt, fileName="default"):
    tts = gTTS(text=txt, lang="hi") #creating instance
    """make directory if not exist"""
    if not os.path.exists("audios"):
        os.mkdir("audios")
    """file naming"""
    if fileName == "default":
        fileName = f"audios/{txt}.mp3".lower()
    else:
        fileName = f"audios/{fileName}.mp3".lower()
    """checking if fileName is not exists then save and play"""
    try:
        if not os.path.exists(fileName):
            tts.save(fileName)
    except:
        playsound("The file your are trying to play is not exist")
def filePlay(data):
    fileName = f"audios/{data}.mp3".lower()
    if os.path.exists(fileName):
        playsound(fileName)
       
if(__name__=='__main__'):
   strEng = "HEllo world how are you"
   strHin = "नमस्ते दुनिया वालों आप कैसे हो"
   string = "The file your are trying to play is not exist"

   fileSave(string) #example1 (strEng as a data)
   filePlay(strEng)