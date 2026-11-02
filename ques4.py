# Display table structure
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(students)")

for row in cur.fetchall():
    print(row)

con.close()