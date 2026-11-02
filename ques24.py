# Calculate average marks
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT AVG(marks) FROM students")

average = cur.fetchone()[0]

print("Average Marks:", average)

con.close()