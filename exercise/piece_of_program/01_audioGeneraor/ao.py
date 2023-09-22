import os
from gtts import gTTS

class audioGenerator:
    def __init__(self):
        """make directory if not exists"""
        if not os.path.exists("audios"):
            os.mkdir("audios")

    def saveEng(self, txt):
        fileName = f"audios/{txt}.mp3".lower()
        if not os.path.exists(fileName):
            tts = gTTS(text=txt)
            tts.save(fileName)

    def saveHin(self, txt, fileName=False):
        """file naming"""
        if fileName == False:
            fileName = f"audios/{txt}.mp3".lower()
        else:
            fileName = f"audios/{fileName}.mp3".lower()
        """Generate audio if not exist"""
        if not os.path.exists(fileName):
            tts = gTTS(text=txt, lang="hi")
            tts.save(fileName)

if __name__ == "__main__":
   strEng = "HEllo world how are you"
   strHin = "नमस्ते दुनिया वालों आप सब कैसे हो"

   ag = audioGenerator()

#    ag.saveEng(strEng)
#    ag.saveHin(strHin)
   ag.saveHin(strHin, strEng)