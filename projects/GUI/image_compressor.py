def getValue(event):
    quality_str.set(event)

def call():
    global data
    data = quality_ent.get()
    if data:
        data = int(data)
        quality_scale.set(data)
    else:
        quality_scale.set(0)
    root.after(100, call)

"""import file"""
def Import():
    from PIL import Image
    global data2
    select_file = filedialog.askopenfile(title="Select file").name
    path_str.set(select_file)
    data2 = path_str.get()
    img = Image.open(data2)
    image = ImageTk.PhotoImage(img)
    lbl.config(image=image)

def compressed():
    from PIL import Image
    
    output = "/home/neo/Desktop/"
    quality = data
    picture = Image.open(data2)
    image = data2.split("/")[-1]
    picture.save(output+image, "JPEG", optimize=True, quality=quality)



from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Image Compressor")
root.geometry("500x400+500+10")

lbl = Label(root, text="Image", bg="yellow")
lbl.place(x=10, y=10, width=480, height=290)

"""Entry"""
path_str = StringVar()
path_ent = Entry(root, textvariable=path_str)
path_ent.place(x=10, y=310, width=402)


"""Import file"""
"""Button"""
path_btn = Button(root, text="Import", command=Import)
path_btn.place(x=425, y=310)

"""Entry"""
quality_str = IntVar()
quality_ent = Entry(root, textvariable=quality_str)
quality_ent.place(x=425, y=350, width=70)

"""Scale"""
quality_scale = Scale(root, from_=0, to=100, length=400, showvalue=False, orient=HORIZONTAL, command=getValue)
quality_scale.place(x=10, y=350)

"""Button"""
save = Button(root, text="Save", command=compressed)
save.pack(side=BOTTOM)

call()

root.mainloop()