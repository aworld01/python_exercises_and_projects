import re

with open("test.txt", "r") as rf:
    data = rf.read().lower()
    data = re.split(r"[.?!\n]", data)
    for line in data:
        if line == "":
            continue
        data = line.lstrip()
        data = data.replace("\n", "")
        print(data)