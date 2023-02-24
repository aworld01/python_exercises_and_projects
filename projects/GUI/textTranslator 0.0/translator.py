import db

def tran(arg):
    clear_output()
    clear_missing()
    data_txt = source.get(1.0, END).lower()
    data_txt = data_txt.split(".")
    for eng in data_txt:
        english = eng.lstrip()
        e = db.search(english) #this may throw None
        """to skip the None"""
        if e == None:
            miss = f"{english}\n"
            insert_eng(miss)
            continue
        en, hi = e
        if english == en:
            hindi = f"{hi}| "
            insert_hin(hindi)

def total():
    # data = lbl_total.cget('text')
    data = lbl_total['text']
    data = f"{data}{db.count()}"
    lbl_total['text'] = data


def clear_output():
    output.delete(1.0, END)

def clear_missing():
    missing.delete(1.0, END)

def insert_hin(hindi):
        output.insert(END, hindi)

def insert_eng(english):
        missing.insert(END, english)

from tkinter import *

root = Tk()
root.geometry("1000x600")
root.title("L2S Translator")

lbl_title = Label(root, text="L2S Translator")
lbl_title.pack()

"""Labels"""
lbl_missing = Label(root, text="Not Found")
lbl_missing.place(relx=0.72, rely=0.08)

lbl_source = Label(root, text="Source")
lbl_source.place(relx=0.24, rely=0.08)

lbl_source = Label(root, text="Output")
lbl_source.place(relx=0.47, rely=0.54)

lbl_total = Label(root, text="Total Sentences: ")
lbl_total.place(relx=0.84, rely=0.04)

total()

"""Button"""
update_btn = Button(root, text="Update database")
update_btn.place(relx=0.02, rely=0.04)


source = Text(root, padx=10, pady=10)
source.place(relx=0.02, rely=0.12, relwidth=0.48, relheight=0.42)

missing = Text(root, padx=10, pady=10)
missing.place(relx=0.50, rely=0.12, relwidth=0.48, relheight=0.42)

output = Text(root, padx=10, pady=10)
output.place(relx=0.02, rely=0.58, relwidth=0.96, relheight=0.40)

"""keybind"""
root.bind("<Control_L><Shift_L>", tran) #Enter: to exit
root.mainloop()