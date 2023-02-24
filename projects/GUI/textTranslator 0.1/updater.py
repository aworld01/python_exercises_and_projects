import db

def tran(arg):
    pass
    # clear_output()
    # clear_missing()
    # data_txt = source.get(1.0, END).lower()
    # data_txt = data_txt.split(".")
    # for eng in data_txt:
    #     english = eng.lstrip()
    #     e = db.search(english) #this may throw None
    #     """to skip the None"""
    #     if e == None:
    #         miss = f"{english}\n"
    #         insert_eng(miss)
    #         continue
    #     en, hi = e
    #     if english == en:
    #         hindi = f"{hi}| "
    #         insert_hin(hindi)

def populate():
    n = 0
    data = db.show()
    for record in data:
        eng, hin = record
        n += 1
        record = f"{n} => {eng} => {hin}"
        database.insert(END, record)

def total():
    # data = lbl_total.cget('text')
    data = lbl_total['text']
    data = f"{data}{db.count()}"
    lbl_total['text'] = data

def clear_notFound():
    notFound.delete(1.0, END)
def clearDatabase():
    database.delete(1.0, END)

def insert_notFound(english):
        notFound.insert(END, english)

from tkinter import *

root = Tk()
root.geometry("1000x600")
root.title("L2S Translator")
root.config(bg="green")

lbl_title = Label(root, text="L2S Translator")
lbl_title.pack(pady=10)

"""Button"""
update_btn = Button(root, text="Home")
update_btn.place(relx=0.02, rely=0.04)

"""Labels"""
lbl_total = Label(root, text="Total => ")
lbl_total.place(relx=0.84, rely=0.04)

"""calling totalFunction"""
total()

lbl_eng = Label(root, text="Eng:")
lbl_eng.place(relx=0.02, rely=0.10)

lbl_hin = Label(root, text="Hin:")
lbl_hin.place(relx=0.02, rely=0.16)

lbl_source = Label(root, text="Source")
lbl_source.place(relx=0.24, rely=0.21)

lbl_notFound = Label(root, text="Not Found")
lbl_notFound.place(relx=0.72, rely=0.21)

lbl_database = Label(root, text="Database")
lbl_database.place(relx=0.48, rely=0.61)

"""Entry"""
ent_eng = Entry(root)
ent_eng.place(relx=0.05, rely=0.10, relwidth=0.93)

ent_hin = Entry(root)
ent_hin.place(relx=0.05, rely=0.16, relwidth=0.93)

"""Text"""
source = Text(root, padx=10, pady=10)
source.place(relx=0.02, rely=0.25, relwidth=0.48, relheight=0.35)

notFound = Text(root, padx=10, pady=10)
notFound.place(relx=0.50, rely=0.25, relwidth=0.48, relheight=0.35)

frm_lbx = Frame(root)
frm_lbx.place(relx=0.02, rely=0.64, relwidth=0.96, relheight=0.35)

"""List box"""
database = Listbox(frm_lbx)
database.place(relheight=1, relwidth=1)
"""Scrollbar"""
scrollbar = Scrollbar(frm_lbx)
scrollbar.pack(side=RIGHT, fill=Y)
database.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=database.yview) #to configure scrollbar

"""calling populate function to insert data"""
populate()

"""keybind"""
root.bind("<Control_L><s>", tran)
root.mainloop()