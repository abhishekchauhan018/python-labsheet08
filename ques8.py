# Insert one student
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    (1, "Abhishek", 22, 85)
)

con.commit()
print("Record inserted successfully")

con.close()