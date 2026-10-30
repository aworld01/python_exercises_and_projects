import psutil

battery = psutil.sensors_battery()
# print(battery)

per = battery.percent
# print(f"{per}%")

per = round(per, 1)
# print(f"{per}%")

def info():
    if per>=75:
        print(f"We have enough power to continue our work")
    elif (per>=40) and (per<=75):
        print(f"We should connect our system to charging point to charge our battery")
    elif (per>=15) and (per<=30):
        print(f"We don't have enough power to work, please connect to charging")
    elif per<=15:
        print(f"we have very low power, please connect to charging the system will shutdown very soon")
        
    print(f"{per}%")
info()