# Update student name
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

student_id = int(input("Enter student ID: "))
name = input("Enter new name: ")

cur.execute(
    "UPDATE students SET name=? WHERE id=?",
    (name, student_id)
)

con.commit()

print("Name updated successfully")

con.close()