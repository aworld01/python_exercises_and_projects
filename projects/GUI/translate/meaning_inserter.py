import dbms

file = "meanings.txt"
with open(file, mode="r", encoding="utf-8") as rf:
    data = rf.read()
    data = data.split("\n")
    for record in data:
        record = record.replace(", ", ",")
        print(record)
        eng, hin = record.split(": ")
        dbms.insertdata(eng, hin)