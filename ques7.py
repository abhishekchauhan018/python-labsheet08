# Check table existence
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
SELECT name FROM sqlite_master
WHERE type='table' AND name=?
""", ("students",))

if cur.fetchone():
    print("Table exists")
else:
    print("Table does not exist")

con.close()