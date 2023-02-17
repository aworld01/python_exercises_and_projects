import psutil

battery = psutil.sensors_battery()
# print(battery)

per = battery.percent
# print(per)

per = round(per, 1)
# print(per)

if per>=75:
    print('We have enough power to continue our work')
elif (per>=40) and (per<=75):
    print('We should connect our system to charging point to charge our battery')
elif (per>=15) and (per<=30):
    print("We don't have enough power to work, please connect to charging")
elif per<=15:
    print("we have very low power, please connect to charging the system will shutdown very soon")