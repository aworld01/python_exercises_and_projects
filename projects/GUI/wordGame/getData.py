def newData(arg):
    db = {}
    with open(arg, mode="r", encoding="utf-8") as rf:
        data = rf.read()
        data = data.split("\n")
        for record in data:
            record = record.replace(", ", ",")
            eng, hin = record.split(": ")
            db.update({eng: hin})
    return db

if __name__ == "__main__":
    file = "sentences.txt"

    for key, value in newData(file).items():
        print(f"{key} => {value}")