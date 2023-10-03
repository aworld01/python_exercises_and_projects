import os
import socket
from gtts import gTTS
from playsound import playsound #pip install playsound

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

obj = audioGenerator()
save = obj.saveHin

"""to check internet connection"""
def net():
    try:
        socket.create_connection(("google.com",80))
        return True
    except OSError:
        return False

def audioCreater(data, name=False):
    if net():
        if name == False:
            save(data)
        else:
            save(data, name)
    else:
        playsound("audios/sir the audio of this data is not present in my database, i need internet access to create new audio. please connect me to the internet and try again.mp3")


if __name__ == "__main__":
   strEng = "Sir the audio of this data is not present in my database, I need internet access to create new audio. Please connect me to the internet and try again"
   strHin = "सर मेरे डेटाबेस में इस डेटा का ऑडियो मौजूद नहीं है, मुझे नया ऑडियो बनाने के लिए इंटरनेट का एक्सेस चाहिए, कृपया मुझे इंटरनेट से कनेक्ट करें फिर दोबारा कोसिस करें।"

   strEng2 = "HEllo world how are you"
   strHin2 = "नमस्ते दुनिया वालों आप सब कैसे हो"

#    ag.saveEng(strEng)
   audioCreater(strHin, strEng)