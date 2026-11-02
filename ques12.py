# Find students scoring above 80
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT * FROM students WHERE marks > ?", (80,))

for row in cur.fetchall():
    print(row)

con.close()