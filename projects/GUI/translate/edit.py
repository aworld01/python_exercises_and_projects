from tkinter import*
from tkinter import messagebox
import dbhelper

"""functions"""
def update():
    inp1 = input1.get()
    inp2 = input2.get()
    if(len(inp1) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    dbhelper.updatedata(inp1, inp2)
    input1.delete(0, END)
    input2.delete(0, END)
    populate()
def add(event):
    inp1 = input1.get()
    inp2 = input2.get()
    if(len(inp1) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    else:
        dbhelper.insertdata(inp1, inp2)
        input1.delete(0, END)
        input2.delete(0, END)
        populate()
        records()
def delete():
    inp1 = input1.get()
    inp2 = input2.get()
    if(len(inp1) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    else:
        dbhelper.deletebyid(inp1)
        input1.delete(0, END)
        input2.delete(0, END)
        populate()
        records()
def populate():
    lbx.delete(0, END)
    for index, rows in enumerate(dbhelper.show()):
        english = rows[1]
        hindi = rows[2]
        data = f"{index}: {english}    =>    {hindi}"
        lbx.insert(END, data)
def records():
    cnt = f"Total: {dbhelper.count1()}"
    total.config(text=cnt)

root = Tk()
root.title("Translator")
# root.geometry("1620x500+1820+0")
root.config(bg="maroon")
root.resizable(0,0)
pt = PhotoImage(file = 'icon.png')
root.iconphoto(False, pt)

main = Frame(root, bg="maroon")
main.pack()

Label(main, text="L2S Translator", font=("Arial",30, "bold")).grid(row=1, column=0, pady=(20, 10), columnspan=2)

total = Label(main, text="Total:", padx=10)
total.grid(row=0, column=1, columnspan=2, sticky=E)
records()

Label(main, text="Eng:", padx=10, bg="maroon", fg="white").grid(row=2, column=0, sticky=W)

input1 = Entry(main, font=("arial", 16, "bold"))
input1.grid(row=2, column=1, ipadx=160, sticky=W)

Label(main, text="Hin:", padx=10, bg="maroon", fg="white").grid(row=3, column=0, sticky=W)

input2 = Entry(main, font=("arial", 16, "bold"))
input2.grid(row=3, column=1, ipadx=160, sticky=W)

Label(main, text="Word Lists", padx=10, bg="maroon", fg="white").grid(row=5, column=1, pady=(10, 0))

"""defining a Frame for listbox"""
frm_lbx2 = Frame(main,bd=2, relief=RIDGE)
frm_lbx2.grid(row=6, column=0, ipadx=300, ipady=100, columnspan=2)

"""defining a Listbox"""
lbx = Listbox(frm_lbx2,font=("arial", 18, "bold"))
lbx.place(x=0, y=0, relwidth=1, relheight=1)

"""defining a Scrollbar"""
scroll2 = Scrollbar(frm_lbx2,orient=VERTICAL)
scroll2.pack(side=RIGHT,fill=Y)

"""to configure scrollbar with listbox"""
lbx.config(yscrollcommand=scroll2.set)
scroll2.config(command=lbx.yview)
populate()

updated = Label(main, text="Last update: 24/03/2022", bg="maroon", fg="white")
updated.grid(row=7, column=0, columnspan=2, pady=(10,0))

frm_btn = Frame(root, bg="maroon")
frm_btn.pack()
upload = Button(frm_btn, text="ADD", command=lambda:add("event"))
upload.grid(row=0, column=0, pady=(10, 0), padx=(0, 50))
upd = Button(frm_btn, text="UPDATE", command=update).grid(row=0, column=1, pady=(10, 0), padx=(0, 50))
delete = Button(frm_btn, text="DELETE", command=delete).grid(row=0, column=2, pady=(10, 0), padx=(0, 50))
close = Button(frm_btn, text="CLOSE", command=root.destroy).grid(row=0, column=3, pady=(10, 0))

root.bind("<Return>", add)

root.mainloop()