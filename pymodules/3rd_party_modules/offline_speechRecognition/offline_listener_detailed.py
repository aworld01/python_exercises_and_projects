"""
CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
CHUNKS = 1024
INDEX=1

stream = mic.open(format=AUDIO_FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                input_device_index=INDEX,
                frames_per_buffer=CHUNKS
                )

"""
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model("vosk-model-small-en-in-0.4")

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
CHUNKS = 1024
INDEX=1

mic = pyaudio.PyAudio() #to initialize pyaudio
    
def listen():
    recognizer = KaldiRecognizer(model, FRAME_RATE)
    stream = mic.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    input_device_index=INDEX,
                    frames_per_buffer=CHUNKS
                    )
    stream.start_stream()
    while True:
        data = stream.read(CHUNKS)
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