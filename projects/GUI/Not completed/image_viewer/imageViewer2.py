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
    global lbl, img_list, next_img, path
    next_img = next_img+1
    lbl.grid_forget()

    img = ImageTk.PhotoImage(Image.open(f"{path}{img_list[next_img]}"))
    print(img)
    
    lbl = Label(root, image=img)
    lbl.grid(row=0, column=0, columnspan=3)

    if next_img == n:
        forward_btn.config(state=DISABLED)
        back_btn.config(state=NORMAL)
    
    root.update(root)


from tkinter import*
from PIL import ImageTk, Image
import os

img_list = os.listdir("images")
n = img_list
path = "images/"
next_img = 0



root = Tk()
root.title("Image Viewer")
img = ImageTk.PhotoImage(Image.open(f"{path}{img_list[0]}"))
print(img)

lbl = Label(root, image=img)
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