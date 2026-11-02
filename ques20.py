# Empty students table
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

# SQLite uses DELETE instead of TRUNCATE
cur.execute("DELETE FROM students")

con.commit()

print("Table emptied successfully")

con.close()