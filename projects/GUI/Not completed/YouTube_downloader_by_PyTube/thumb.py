from tkinter import*
from pytube import*
from PIL import Image, ImageTk

url = "https://www.youtube.com/watch?v=c_2FOaQRW6o"
yt = YouTube(url)
# thumbnail = yt.thumbnail_url #to fetch thumbnail of video.

# img = Image.open(thumbnail) #make object
# image = ImageTk.PhotoImage(img) #to make tkinter compatible

root = Tk()
root.title("")
root.geometry("600x400")
"""Label"""
lbl = Label(root)
lbl.pack(pady=20, ipadx=300, ipady=300)

mainloop()