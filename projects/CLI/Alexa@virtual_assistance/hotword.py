import os
from listener import listen

while True:
    print("sleeping...")
    wakeup=listen()
    if "wake up" in wakeup:
        os.system("python3 alexa.py")