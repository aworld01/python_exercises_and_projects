import whisper #pip install whisper
import sounddevice as sd #pip install sounddevice
import wavio as wv #pip install wavio
from playsound import playsound #pip install playsound

model = whisper.load_model("base.en") #to load the model (download if not exists)

def recorder():
    freq = 44100
    duration = 5 #in seconds

    print("Recording...")
    recording = sd.rec((duration*freq), samplerate=freq, channels=2)
    sd.wait()

    wv.write(f"temp.wav", recording, freq, sampwidth=2)
    # print("Your recording has been completed")

def Listener():
      recorder()
      result = model.transcribe("temp.wav")
      return result["text"]

while True:
      result = Listener().lower()
      print(f"You: {result}")
      if "how are you" in result:
            print(f"Alexa: Hi sir I am fine, thank you")
      elif "what are you doing" in result:
            print(f"Alexa: Just talking with you sir")
      elif "how old are you" in result:
            print(f"Alexa: I am just 18 sir")
      elif "stop listening" in result:
            print(f"Alexa: Thank you sir, see you again!")
            break
      elif "you need a break" in result:
            print(f"Alexa: Thank you sir, see you again!")
            break
