# Display top 3 students
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3
""")

for row in cur.fetchall():
    print(row)

con.close()