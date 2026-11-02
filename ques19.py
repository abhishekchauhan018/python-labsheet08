# Delete students scoring below 40
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("DELETE FROM students WHERE marks < 40")

con.commit()

print("Students with marks below 40 deleted")

con.close()