# Delete student by ID
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

student_id = int(input("Enter student ID: "))

cur.execute("DELETE FROM students WHERE id=?", (student_id,))

con.commit()

print("Student deleted successfully")

con.close()