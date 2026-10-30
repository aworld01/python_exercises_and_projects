"""
print(spr.__version__) #validate the installation

mic=spr.Microphone() #create an object of Recognizer
os.system("clear") #to clear the terminal
print(mic.list_microphone_names()) #to check mics in your computer.

mic=spr.Microphone(device_index=0) #to select a particular microphone.
"""
import speech_recognition as spr #pip install SpeechRecognition

r = spr.Recognizer()
info = spr.AudioFile("sound.wav")

with info as source:
    # spr.adjust_for_ambient_noise(source) #to remove noise from audio
    audio_data = spr.record(source)
    lis = spr.recognize_google(audio_data) #to recognize any speech in the 
print(lis)