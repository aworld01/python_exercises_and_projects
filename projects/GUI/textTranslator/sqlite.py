import sqlite3

con = sqlite3.connect("dictionary.db")

def show():
    tables = con.execute("SELECT * FROM dict")
    return tables

data = ""
for _,eng,hin in show():
    data += f"{eng} => {hin}\n"

with open('temp.txt',mode='w',encoding="utf-8") as rf:
    rf.write(data)