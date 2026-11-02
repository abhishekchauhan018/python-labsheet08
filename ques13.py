# Sort students by marks
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT * FROM students ORDER BY marks DESC")

for row in cur.fetchall():
    print(row)

con.close()