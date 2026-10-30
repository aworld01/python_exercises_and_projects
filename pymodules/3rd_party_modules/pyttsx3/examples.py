import pyttsx3

strEng = "I will speak this text"
strEng2 = "Hello world, how are you?"
strHin = "नमस्ते दुनिया वालों, मेरा नाम अब्दुल ज़ोहा है। आप कैसे हैं?"

"""very basic"""
# def winSpeak(txt):
#     engine = pyttsx3.init() #creating instance
#     engine.say(txt)
#     engine.runAndWait()
# winSpeak(strEng2)


def winSpeak2(txt):
    engine = pyttsx3.init() #creating instance
    
    voices = engine.getProperty('voices')       #getting details of current voice
    # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
    engine.say(txt)
    engine.runAndWait()
winSpeak2(strHin)


"""example2"""
def winSpeak(txt):
    engine = pyttsx3.init() # object creation
    """RATE"""
    rate = engine.getProperty('rate') #getting details of current speaking rate
    print (rate)                      #printing current voice rate
    engine.setProperty('rate', 125)   #setting up new voice rate
    print(rate)
# winSpeak(strEng)


"""example3"""
# def winSpeak(txt):
#     engine = pyttsx3.init() # object creation
#     """VOLUME"""
#     volume = engine.getProperty('volume')   #getting details of current speaking rate
#     print(volume)                           #printing current voice rate
#     engine.setProperty('volume',1.0)        #setting up volume level  between 0 and 1
#     print(volume)
# winSpeak(strEng)


"""example4"""
# def winSpeak(txt):
#     engine = pyttsx3.init() # object creation
#     """VOICE"""
#     voices = engine.getProperty('voices')   #getting details of available voices
#     print(voices)                           #printing voices details
# winSpeak(strEng)

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# # #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[2].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()