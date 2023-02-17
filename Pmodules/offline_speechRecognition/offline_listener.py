from vosk import Model, KaldiRecognizer
import pyaudio

model = Model("vosk-model-small-en-in-0.4")

def listen():
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            txt = text[14:-3]
            if len(txt) > 0:
                print(f"You said: {txt}")
                return txt

if __name__ == "__main__":
    while True:
        query = listen()

        if "how are you" in query:
            print("I'm fine sir")
        elif "what's your name" in query:
            print("My name is Alexa sir")
        elif "take a break" in query:
            print("Thank you sir")
            break