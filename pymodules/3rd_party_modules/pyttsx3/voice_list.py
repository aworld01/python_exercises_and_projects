import os
import pyttsx3

engine = pyttsx3.init()
for voice in engine.getProperty("voices"):
    voice = os.path.split(voice.id)[-1]
    print(voice)