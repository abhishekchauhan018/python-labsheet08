# Update student marks
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

student_id = int(input("Enter student ID: "))
marks = float(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks=? WHERE id=?",
    (marks, student_id)
)

con.commit()

print("Marks updated successfully")

con.close()