import sounddevice as sd #pip install sounddevice
from scipy.io.wavfile import write #pip install scipy
import wavio as wv #pip install wavio


def Record():
    freq = 44100
    duration = 5 #in seconds
    
    print("Recording...")
    recording = sd.rec((duration*freq), samplerate=freq, channels=2)
    sd.wait()

    write(f"scipy.wav", freq, recording)

    wv.write(f"wavio.wav", recording, freq, sampwidth=2)
    print("Your recording has been completed")

if __name__ == "__main__":
        Record()