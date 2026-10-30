from speaker2 import speak

def Time():
    from datetime import datetime
    time=datetime.now()
    time=time.strftime("%H:%M")
    print(f"The time is: {time}")
    speak(f"the time is: {time}")

if __name__ == "__main__":
    Time()