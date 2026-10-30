from playsound import playsound #pip install playsound

fileName = "मेरा नाम एलेक्सा है.mp3"

# playsound(fileName) #example1

"""example2"""
for i in range(5):
    print(f"{i} {fileName}")
    playsound(fileName)