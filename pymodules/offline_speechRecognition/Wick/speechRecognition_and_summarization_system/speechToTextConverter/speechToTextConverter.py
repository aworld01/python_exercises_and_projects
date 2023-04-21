"""
pip install pydub
pip install vosk

Speech Recognition And Summarization System In Python [Project Tutorial]
15:00/44:37
"""
import os
import json
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

frameRate = 16000
channel = 1
model = Model("vosk-model-small-en-us-0.15")
file = "test.mp3"

"""to converting data that vosk required (pip install pydub)"""
def conv(file):
    mp3 = AudioSegment.from_mp3(file)
    mp3 = mp3.set_channels(channel)
    mp3 = mp3.set_frame_rate(frameRate)
    data = mp3.raw_data #it returns result into binary representation.
    return data

"""to print binary data (only for check)"""
# d = conv(file)
# print(d)

"""to recognise the data (pip install vosk)"""
def recog(r_data):
    os.system("cls") #to clear terminal after calling the function
    rec = KaldiRecognizer(model, frameRate)
    rec.SetWords(True)
    rec.AcceptWaveform(r_data)
    result = rec.Result() #returns result into json form
    # print(result) #only for check

    """using json to convert data into string form"""
    text = json.loads(result)["text"] #converting data into string form
    # print(text) #only for check
    return text


data = conv(file)
txt = recog(data)
print(txt) #only for check