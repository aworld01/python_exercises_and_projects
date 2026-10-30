import pyttsx3 #pip install pyttsx3

def say(txt):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[1].id)
    engine.setProperty("rate", 170)
    engine.say(text=txt)
    engine.runAndWait()


if __name__ == "__main__":
    string = "Hello world how are you? My name is Abdul Zoha, what is your name please?"
    say(string)