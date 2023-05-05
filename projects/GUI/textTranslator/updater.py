import db

def trans():
    clear_notFound()
    clear_database()
    """filtering Data"""
    data_txt = source.get(1.0, END).lower()
    data_txt = data_txt.split(".")
    for eng in data_txt:
        english = eng.lstrip()
        e = db.search(english) #it may throw None
        """to skip the None"""
        if e == None:
             miss = f"{english}\n"
             insert_eng(miss)
             continue
    populate()
    
def update(arg):
    clear_database()
    english = ent_eng.get()
    hindi = ent_hin.get()
    e = db.search(english) #it may throw None
    """to skip the None"""
    if e == None:
        if english:
            if hindi:
                db.insert(english, hindi)
    trans()

def populate():
    n = 0
    data = db.show()
    for record in data:
        eng, hin = record
        n += 1
        record = f"{n}:   {eng}   =>   {hin}"
        database.insert(END, record)

def total():
    # data = lbl_total.cget('text')
    data = lbl_total['text']
    data = f"{data}{db.count()}"
    lbl_total['text'] = data

def clear_notFound():
    notFound.delete(1.0, END)

def clear_database():
    database.delete(0, END)

def insert_eng(english):
    notFound.insert(END, english)

from tkinter import *

root = Tk()
root.geometry("1000x600")
root.title("L2S Translator")
root.config(bg="green")

lbl_title = Label(root, text="L2S Translator")
lbl_title.pack(pady=10)

"""Labels"""
lbl_total = Label(root, text="Total => ")
lbl_total.place(relx=0.92, rely=0.01)

lbl_eng = Label(root, text="Field1:")
lbl_eng.place(relx=0.02, rely=0.07)

lbl_hin = Label(root, text="Field2:")
lbl_hin.place(relx=0.02, rely=0.12)

"""Entry"""
ent_eng = Entry(root)
ent_eng.place(relx=0.08, rely=0.07, relwidth=0.90)

ent_hin = Entry(root)
ent_hin.place(relx=0.08, rely=0.12, relwidth=0.90)

"""Text"""
source = Text(root, padx=10, pady=10)
source.place(relx=0.02, rely=0.17, relwidth=0.96, relheight=0.38)

notFound = Text(root, padx=10, pady=10)
notFound.place(relx=0.02, rely=0.56, relwidth=0.49, relheight=0.37)

frm_lbx = Frame(root)
frm_lbx.place(relx=0.52, rely=0.56, relwidth=0.46, relheight=0.37)

"""List box"""
database = Listbox(frm_lbx)
database.place(relheight=1, relwidth=1)
"""Scrollbar"""
scrollbar = Scrollbar(frm_lbx)
scrollbar.pack(side=RIGHT, fill=Y)
database.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=database.yview) #to configure scrollbar

"""Frame"""
btn_frm = Frame(root)
btn_frm.place(relx=0.3, rely=0.94, relwidth=0.45, relheight=0.05)

"""Button"""
add_btn = Button(btn_frm, text="Check", command=trans)
add_btn.place(relwidth=0.25, relheight=1)

update_btn = Button(btn_frm, text="Add")
update_btn.place(relx=0.25, relwidth=0.25, relheight=1)

update_btn = Button(btn_frm, text="Update")
update_btn.place(relx=0.50, relwidth=0.25, relheight=1)

update_btn = Button(btn_frm, text="Delete")
update_btn.place(relx=0.75, relwidth=0.25, relheight=1)

"""calling functions"""
populate()
total()

# """keybind"""
# root.bind("<Control_L><s>", update)
# root.bind("<Control_L><t>", trans)
root.mainloop()