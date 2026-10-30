import sounddevice as sd #pip install sounddevice
import wavio as wv #pip install wavio
import datetime


def Record():
    freq = 44100
    duration = 5 #in seconds
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d %H_%M_%S")
    
    print("Recording...")
    recording = sd.rec((duration*freq), samplerate=freq, channels=2)
    sd.wait()

    wv.write(f"recordings/{filename}.wav", recording, freq, sampwidth=2)
    print("Your recording has been completed")

if __name__ == "__main__":
    while True:
        Record()