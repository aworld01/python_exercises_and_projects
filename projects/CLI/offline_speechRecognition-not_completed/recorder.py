import sounddevice as sd
import wavio as wv
import datetime as dt

freq = 44100
duration = 5 #in seconds

print("Recording...")

while True:
    ts = dt.datetime.now()
    filename = ts.strftime("%Y-%m-%d %H-%M-%S")
    print(filename)

    """start recorder with the given values of duration and sample frequency"""
    recording = sd.rec(int(duration*freq), samplerate=freq, channels=1)

    """record audio for the given number of seconds"""
    sd.wait()

    """convert the numpy array to audio file"""
    wv.write(f"./recordings/{filename}.wav", recording, freq, sampwidth=2)