# Group students by age
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
""")

for row in cur.fetchall():
    print("Age:", row[0], "Count:", row[1])

con.close()