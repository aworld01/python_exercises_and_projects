from tkinter import*
import speech_recognition as sr



"""SpeechRecognition..."""
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        lbl.config(text="Listing...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=2,phrase_time_limit=5)
    try:
        lbl.config(text="Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        lbl.config(text=f"Your command: {query}")
    except:
        return ""
    return query.lower()

root = Tk()
root.title("Speech Recognition")
root.geometry("600x400+1200+10")

"""Label"""
lbl = Label(root, text="test")
lbl.pack(pady=20)
"""Button"""
btn = Button(root, text="Click", command=listen)
btn.pack(pady=50)

root.mainloop()