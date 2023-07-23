import sqlite3

con = sqlite3.connect('source_code/trans.db')
query = """CREATE TABLE IF NOT EXISTS trans(
    eng TEXT,
    hin TEXT
)"""
con.execute(query)
cur = con.cursor()

def structure():
    query = "schema translate"
    data = cur(query)
    print(data)


def show():
    d = con.execute("SELECT * FROM translate")
    return [results for results in d]

def insert(eng, hin):
    query = "INSERT INTO translate(eng, hin) VALUES(?,?)"
    con.execute(query, (eng, hin))
    con.commit()

def delete(eng):
    query = "DELETE FROM translate WHERE eng = ?"
    con.execute(query, (eng,))
    con.commit()

def update(eng, hin):
    query = "UPDATE translate SET hin = ? WHERE eng = ?"
    con.execute(query, (hin, eng))
    con.commit()

def trans_search(arg):
    query = "SELECT eng FROM translate WHERE eng = ?"
    d = con.execute(query, (arg,))
    for item in d:
        return item
    
if __name__ == "__main__":
    # structure() #not working

    # data = show()
    # print(data)

    # insert("I love my Cat", "Main apni billi ko pyar karta hun")

    d = trans_search("How are you?")
    print(d)