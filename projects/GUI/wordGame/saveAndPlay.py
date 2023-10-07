import os
import socket
from gtts import gTTS
from playsound import playsound #pip install playsound

class audioGenerator:
    def __init__(self):
        """make directory if not exists"""
        if not os.path.exists("audios/hindi"):
            os.makedirs("audios/hindi")
        if not os.path.exists("audios/english"):
            os.makedirs("audios/english")

    def saveEnglish(self, txt):
        fileName = f"audios/english/{txt}.mp3".lower()
        if not os.path.exists(fileName):
            tts = gTTS(text=txt)
            tts.save(fileName)

    def saveHindi(self, txt, fileName=False):
        """file naming"""
        if fileName == False:
            fileName = f"audios/hindi/{txt}.mp3".lower()
        else:
            fileName = f"audios/hindi/{fileName}.mp3".lower()
        """Generate audio if not exist"""
        if not os.path.exists(fileName):
            tts = gTTS(text=txt, lang="hi")
            tts.save(fileName)

obj = audioGenerator()
saveIntoHindi = obj.saveHindi
saveIntoEnglish = obj.saveEnglish

"""to check internet connection"""

def playHin(data):
    data = f"audios/hindi/{data}.mp3"
    if os.path.exists(data):
        playsound(data)

def playEng(data):
    data = f"audios/english/{data}.mp3"
    print(data)
    if os.path.exists(data):
        playsound(data)

def net():
    try:
        socket.create_connection(("google.com",80))
        return True
    except OSError:
        return False

def saveHin(data, name=False):
    if net():
        if not name == False:
            saveIntoHindi(data, name)
        else:
            saveIntoHindi(data)
    else:
        playsound("audios/hindi/sir the audio of this data is not present in my database, i need internet access to create new audio. please connect me to the internet and try again.mp3")


def saveEng(data):
    if net():
        saveIntoEnglish(data)
    else:
        playsound("audios/english/sir the audio of this data is not present in my database, i need internet access to create new audio. please connect me to the internet and try again.mp3")


if __name__ == "__main__":

   strEng = "HEllo world how are you"
   strHin = "नमस्ते दुनिया वालों आप सब कैसे हो"

   strEng1 = "Sir the audio of this data is not present in my database, I need internet access to create new audio. Please connect me to the internet and try again"
   strHin1 = "सर मेरे डेटाबेस में इस डेटा का ऑडियो मौजूद नहीं है, मुझे नया ऑडियो बनाने के लिए इंटरनेट एक्सेस का जरुरत पड़ता है, कृपया मुझे इंटरनेट से कनेक्ट करें फिर दोबारा कोसिस करें।"

   strEng2 = "The audio files have been updated successfully"
   strHin2 = "ऑडियो फ़ाइलें सफलतापूर्वक अपडेट कर दी गई हैं"

#    ag.saveEng(strEng)
   saveHin(strHin2, strEng2)