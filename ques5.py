# Display all tables
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
""")

for row in cur.fetchall():
    print(row[0])

con.close()