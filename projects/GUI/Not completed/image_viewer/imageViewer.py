def back():
    global lbl, back_btn, next_img
    next_img = next_img-1
    lbl.grid_forget()

    lbl = Label(root, image=img_list[next_img])
    lbl.grid(row=0, column=0, columnspan=3)

    if next_img == 0:
        forward_btn.config(state=NORMAL)
        back_btn.config(state=DISABLED)
def forward():
    global lbl, img_list, next_img
    next_img = next_img+1
    lbl.grid_forget()

    lbl = Label(root, image=img_list[next_img])
    lbl.grid(row=0, column=0, columnspan=3)

    if next_img == 4:
        forward_btn.config(state=DISABLED)
        back_btn.config(state=NORMAL)


from tkinter import*
from PIL import ImageTk, Image
import os

img_list = os.listdir("images/")
path = "images/"

next_img = 0

root = Tk()
root.title("Image Viewer")

img1 = ImageTk.PhotoImage(Image.open("images/image1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/image2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/image3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/image4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/image5.jpg"))

img_list = [img1, img2, img3, img4, img5]
n = len(img_list)

lbl = Label(root, image=img_list[next_img])
lbl.grid(row=0, column=0, columnspan=3)

"""assign buttons"""
back_btn = Button(root, text="<<", command=back, state=DISABLED)
exit_btn = Button(root, text="Exit", command=root.quit)
forward_btn = Button(root, text=">>", command=forward)
"""calling buttons"""
back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2)

root.mainloop()