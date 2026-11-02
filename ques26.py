# Export database records to CSV
import sqlite3
import csv

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT * FROM students")
data = cur.fetchall()

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["ID", "Name", "Age", "Marks"])
    writer.writerows(data)

print("Data exported to CSV successfully")

con.close()