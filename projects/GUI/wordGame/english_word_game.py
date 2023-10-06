from tkinter import*
from tkinter import messagebox
from prePro import dataPro
import random
from saveAndPlay import saveHin, saveEng, playHin, playEng

data = dataPro("database.txt")
eng = tuple(data.keys())
hin = tuple(data.values())
length = len(eng)

hit = 0
miss = 0
total = 0
n = len(eng)
num = random.randrange(0,n,1)

"""functions"""
def count_data():
    dt.config(text=f"Total data: {n}")
def default():
    global eng, hin, num
    lbl.config(text=hin[num])
def reset():
    global hin, eng, num
    num = random.randrange(0,n,1)
    lbl.config(text=hin[num])
    
    playHin(eng[num])
    saveHin(hin[num], eng[num])

    ans.config(text="")
    ent.delete(0, END)
def check(key):
    global hin, eng, num, hit, total, miss

    word = ent.get().lower()
    if word == eng[num]:
        ent.delete(0, END)
        hit += 1
        total += 1
        hit_lbl.config(text=f"{hit}")
        total_lbl.config(text=f"{total}")
        reset()
    elif word == "":
        messagebox.showinfo("Information", "The User input can't be empty")
    elif word == "exit()":
        root.destroy()
    else:
        rigAns = f"The right answer is: {eng[num].capitalize()}"
        ans.config(text=rigAns)
        miss += 1
        hit += 1
        total += 1
        mis_lbl.config(text=f"{miss}")
        hit_lbl.config(text=f"{hit}")
        total_lbl.config(text=f"{total}")
        ent.delete(0, END)

root = Tk()
root.title("English Word Game")
root.geometry("900x500+1020+10")
root.config(bg="#000000")
"""Label"""
lbl = Label(root, font=("Verdana", 18), bg="#000000", fg="#ffffff")
lbl.pack(pady=40)
"""Entry"""
ent = Entry(root, font=("verdana", 16))
ent.pack(ipadx=300)

frm = Frame(root, bg="#000000")
frm.pack(pady=(40, 0))

Label(frm, text="Hit: ", bg="#000000", fg="#ffffff").grid(row=0, column=0, sticky=W)
hit_lbl = Label(frm, text="O", bg="#000000", fg="#ffffff")
hit_lbl.grid(row=0, column=1)

Label(frm, text="Miss: ", bg="#000000", fg="#ffffff").grid(row=1, column=0, sticky=W)
mis_lbl = Label(frm, text="O", bg="#000000", fg="#ffffff")
mis_lbl.grid(row=1, column=1)

Label(frm, text="Total: ", bg="#000000", fg="#ffffff").grid(row=2, column=0, sticky=W)
total_lbl = Label(frm, text="O", bg="#000000", fg="#ffffff")
total_lbl.grid(row=2, column=1)

"""Label"""
ans = Label(root, font=("Verdana", 18), bg="#000000", fg="#ffffff")
ans.pack(pady=40)

dt = Label(root, font=("Verdana", 18), bg="#000000", fg="#ffffff")
dt.pack(pady=40)


root.bind("<Return>", check) #Enter check
default()
count_data()

root.mainloop()