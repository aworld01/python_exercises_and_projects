source = {
    "how are you": "आप कैसे हैं",
    "what is your name": "आपका क्या नाम है",
    "how old are you": "आपकी आयु कितनी है",
    "long long ago": "बहुत समय पहले"
    }

"""example-1"""
# data = ["how are you", "how old are you", "what is your name", "how old are you"]

# for q in data:
#         if q in source:
#             print(f"{source[q]}", end=". ")



"""example-2"""
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
        if s in source:
            st = source[s]
            write('destination.txt', st)
d = tran(d)