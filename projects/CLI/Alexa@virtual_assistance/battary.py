from speaker import speak
import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
percentage=float(f'{percentage:.1f}')

def batt():
    print(f"we have {percentage}% battary")
    if percentage>=75:
        speak('We have enough power to continue our work')
    elif percentage>=40 and percentage<=75:
        speak('We should connect our system to charging point to charge our battery')
    elif percentage>=15 and percentage<=30:
        speak("We don't have enough power to work, please connect to charging")
    elif percentage<=15:
        speak("we have very low power, please connect to charging the system will shutdown very soon")
