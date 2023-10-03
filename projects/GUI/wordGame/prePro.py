def dataPro(arg):
    db = {}
    with open(arg, mode="r", encoding="utf-8") as rf:
        data = rf.read()
        # print(data, type(data))

    data = data.split("\n") #split data throw newline
    # print(data, type(data))

    data = [i.strip() for i in data] #remove whitespaces for both side of items
    # print(data)

    data = [i for i in data if i != ""] #to remove empty items
    # print(data)

    """split by ": " and add into dictionary"""
    for i in data:
        eng, hin = i.split(":")
        eng = eng.strip()
        hin = hin.strip()
        db.update({eng:hin})

    return db



if __name__ == "__main__":
    file = "database.txt"
    # dataPro(file)

    for key, value in dataPro(file).items():
        print(f"{key}check => {value}check")
    print("Done")