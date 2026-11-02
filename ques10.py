# Display all students
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT * FROM students")

for row in cur.fetchall():
    print(row)

con.close()