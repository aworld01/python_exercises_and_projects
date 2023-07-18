import sqlite3

con = sqlite3.connect('dict.db')
query = """CREATE TABLE IF NOT EXISTS dictionary(
    eng TEXT,
    hin TEXT
)"""
con.execute(query)

cur = con.cursor()

def structure():
    query = "schema dictionary"
    data = cur(query)
    print(data)
# structure()


def show():
    d = con.execute("SELECT * FROM dictionary")
    return [results for results in d]

def insert(eng, hin):
    query = "INSERT INTO dictionary(eng, hin) VALUES(?,?)"
    con.execute(query, (eng, hin))
    con.commit()

def delete(eng):
    query = "DELETE FROM dictionary WHERE eng = ?"
    con.execute(query, (eng,))
    con.commit()

def update(eng, hin):
    query = "UPDATE dictionary SET hin = ? WHERE eng = ?"
    con.execute(query, (hin, eng))
    con.commit()
    
if __name__ == "__main__":
    # structure() #not working

    data = show()
    print(data)