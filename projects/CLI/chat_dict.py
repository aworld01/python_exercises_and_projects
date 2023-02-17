import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
percentage=float(f'{percentage:.1f}')
per=f"\tSir our system has {percentage} percent battery"

data={
    "hi":"hello sir!",
    "hello":"hi sir!",
    "how are you?":"I'm fine sir",
    "who are you?":"I'm a computer program, my name is Alexa",
    "what is your name?":"My name is Alexa, please tell me how may I help you?",
    "how old are you?":"I'm 18 years old now sir!",
    "goodbye alexa":"Shutting down, thank you sir!"
}
while True:
    d=input('Ask you question: ').lower()
    usr_input=input('Ask you question: ').lower()

    for question in data:
        answer = data[question]

    if usr_input in question:
        print('\t',answer)
    elif usr_input in question:
        break
        print('\t',a)
    elif usr_input in 'how much battary do we have?':
        print(per, end=', ')
        if percentage>=75:
            print('We have enough power to continue our work')
        elif percentage>=40 and percentage<=75:
            print('We should connect our system to charging point')
        elif percentage>=15 and percentage<=30:
            print("We don't have enough power to work, please connect to charging")
        elif percentage<=15:
            print("we have very low power, please connect to charging the system will shutdown very soon")