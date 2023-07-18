import sqlite3

con = sqlite3.connect('trans.db')
query = """CREATE TABLE IF NOT EXISTS translate(
    eng TEXT,
    hin TEXT
)"""
con.execute(query)

cur = con.cursor()

def structure():
    query = "schema translate"
    data = cur(query)
    print(data)
# structure()


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
    
if __name__ == "__main__":
    # structure() #not working

    data = show()
    print(data)