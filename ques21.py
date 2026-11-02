# Create courses table and insert records
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT
)
""")

data = [
    (1, 1, "Python"),
    (2, 2, "Java"),
    (3, 3, "C++"),
    (4, 4, "SQL")
]

cur.executemany(
    "INSERT OR REPLACE INTO courses VALUES (?, ?, ?)",
    data
)

con.commit()

print("Courses table created and data inserted")

con.close()