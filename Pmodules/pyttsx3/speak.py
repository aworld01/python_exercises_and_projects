'''
import pyttsx3 #pip install pyttsx3

"""SPEAK"""
pyttsx3.speak("I will speak this text") #to run dufault voice in one line of code


engine = pyttsx3.init() #object creation

"""to run default voice in multiline of code"""
engine.say("I will speak this text")
engine.runAndWait()




"""RATE"""
rate = engine.getProperty('rate') #getting details of current speaking rate
print (rate)
engine.setProperty('rate', 125) #setting up new voice rate






rate = engine.getProperty('rate') #getting details of current speaking rate
print (rate) #printing current voice rate

engine.say("Hello world, how are you")
engine.runAndWait()

engine.setProperty('rate', 125) #setting up new voice rate

voices=engine.getProperty('voices') #to get list of voices
print(voices) #to print voices

voice=engine.getProperty('voices')[1].id #to get full details about any specific voice.
print(voice)

pyttsx3.speak("hello sir") #to run dufault voice in one line of code
'''

import pyttsx3 #pip install pyttsx3

engine=pyttsx3.init('sapi5')



"""RATE"""
engine.say("I will speak this text")
rate = engine.getProperty('rate') #getting details of current speaking rate
engine.setProperty('rate', 50) #setting up new voice rate
engine.runAndWait()

# rate = engine.getProperty('rate') #getting details of current speaking rate
# print (rate)
# engine.setProperty('rate', 125) #setting up new voice rate

# voice=engine.getProperty('voices')[1].id

# def speak(arg):
#     engine=pyttsx3.init('sapi5')
#     voice=engine.getProperty('voices')[1].id
#     engine.setProperty('voice', voice)
#     engine.say(arg)
#     engine.runAndWait()

# if __name__=="__main__":
#     input = "hello how are you"
#     if "hello how are you" in input:
#         speak("I am fine sir")