import speech_recognition as s # pip install speechrecognition
import os

def listen():
    r = s.Recognizer() #create an object of Recognizer
    with s.Microphone() as mic:
        print("Listening.....")
        # sr.pause_threshold = 1

        audio = r.listen(mic, timeout=2, phrase_time_limit=5)
        try:
            print("Recognizing......")
            query = r.recognize_google(audio, language="en-in")
            print(f"Your command: {query}")
        except:
            return ""
        return query.lower()

if __name__ == "__main__":
    while True:
        query=listen()
        if "how are you" in query:
            print("I'm fine sir")
        elif "take a break" in query:
            os.system("clear")
            break
        elif "go to bed" in query:
            os.system("clear")