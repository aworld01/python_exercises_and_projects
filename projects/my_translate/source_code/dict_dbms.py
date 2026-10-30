import sqlite3

con = sqlite3.connect('source_code/dict.db')
query = """CREATE TABLE IF NOT EXISTS dictionary(
    eng TEXT,
    hin TEXT
)"""
cur = con.cursor()
cur.execute(query)

def structure():
    query = "schema dictionary"
    data = cur(query)
    print(data)
# structure()


def show():
    cur.execute("SELECT * FROM dictionary")
    return [results for results in cur]

def insert(eng, hin):
    query = "INSERT INTO dictionary(eng, hin) VALUES(?,?)"
    cur.execute(query, (eng, hin))
    con.commit()

def delete(eng):
    query = "DELETE FROM dictionary WHERE eng = ?"
    cur.execute(query, (eng,))
    con.commit()

def update(eng, hin):
    query = "UPDATE dictionary SET hin = ? WHERE eng = ?"
    cur.execute(query, (hin, eng))
    con.commit()

def dict_search(arg):
    query = "SELECT eng FROM dictionary WHERE eng = ?"
    cur.execute(query, (arg,))
    for item in cur:
        return item
    
if __name__ == "__main__":
    print(show())