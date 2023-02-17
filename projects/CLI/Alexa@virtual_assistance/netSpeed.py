##pip install speedtest-cli
import speedtest
from speaker2 import speak


def speedTest():
    print("Checking speed.....")
    speak("checking speed")
    speed=speedtest.Speedtest()
    d=speed.download()
    downloading=int(d/800000)
    u=speed.upload()
    uploading=int(u/800000)
    print(f"The Downloading speed is: {downloading} mbps")
    print(f"The uploading speed is: {uploading} mbps\n")
    speak(f"the downloading speed is {downloading} mbps")
    speak(f"the uploading speed is {uploading} mbps")