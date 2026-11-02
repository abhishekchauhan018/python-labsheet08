# Delete students table
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS students")

con.commit()
print("Table deleted successfully")

con.close()