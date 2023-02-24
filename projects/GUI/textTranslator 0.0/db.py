import sqlite3

con = sqlite3.connect("sqlite.db")
query = """CREATE TABLE IF NOT EXISTS tran(
    eng TEXT,
    hin TEXT
)"""
con.execute(query)

def show():
    tables = con.execute("SELECT * FROM tran")
    return tables

def insert(eng, hin):
    query = "INSERT INTO tran(eng, hin) VALUES(?,?)"
    con.execute(query, (eng, hin))
    con.commit()

def delete(eng):
    query = "DELETE FROM tran WHERE eng = ?"
    con.execute(query, (eng,))
    con.commit()

def update(eng, hin):
    query = "UPDATE tran SET eng = ?, hin = ?"
    con.execute(query, (eng, hin))
    con.commit()

def search(inp):
    query = "SELECT * FROM tran WHERE eng = ?"
    data = con.execute(query, (inp,))
    for item in data:
        return item
def count():
    tables = con.execute("SELECT COUNT(*) FROM tran")
    for i in tables:
        return i[0]


if __name__ == "__main__":
    # insert("how old are you", "आपकी आयु कितनी है") #to insert

    # delete("how old are you") #to delete

    """to search"""
    # s = search("what is your name")
    # print(s)

    """to check all the records"""
    # d = show()
    # for records in d:
    #     print(records)

    print(count())