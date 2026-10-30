import db

"""to check a specific record"""
source = db.search("what is your name")

def read(sour):
    with open(sour, "r") as rf:
        data = rf.read()
        data = data.split(".")
        return data
d = read("source.txt")

def write(dest, s):
    with open(dest, encoding="utf-8", mode="a") as wf:
        da = wf.write(f"{s}| ")

def clear(dest):
    with open(dest, "w") as wf:
        wf.write("")


def tran(inp):
    clear("destination.txt")
    for q in inp:
        s = q.lstrip()
        e = db.search(s) #this may throw None

        """to skip the None"""
        if e == None:
            continue

        en, hi = e
        print(hi, en)
        write("destination.txt", hi)
        # for data in source:
        #     print(data)
        # if s in source:
#             st = source[1]
#             write('destination.txt', st)
d = tran(d)