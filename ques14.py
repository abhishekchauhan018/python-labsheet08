# Count student records
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")

count = cur.fetchone()[0]

print("Total Students:", count)

con.close()