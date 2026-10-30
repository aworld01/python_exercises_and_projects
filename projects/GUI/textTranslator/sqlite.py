import sqlite3

con = sqlite3.connect("sqlite.db")

def show():
    tables = con.execute("SELECT * FROM tran")
    return tables

data = ""
for eng,hin in show():
    data += f"{eng} => {hin}\n"

with open('temp2.txt',mode='w',encoding="utf-8") as rf:
    rf.write(data)