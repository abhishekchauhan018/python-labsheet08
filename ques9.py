# Insert multiple students
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

data = [
    (2, "Rahul", 21, 90),
    (3, "Aman", 22, 78),
    (4, "Vikas", 23, 88)
]

cur.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)", data
)

con.commit()
print("Multiple records inserted")

con.close()