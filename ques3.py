# Create students table
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

con.commit()
print("Table created successfully")

con.close()ques