# Import CSV data into database
import sqlite3
import csv

con = sqlite3.connect("student_db.db")
cur = con.cursor()

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        cur.execute("""
        INSERT OR REPLACE INTO students
        (id, name, age, marks)
        VALUES (?, ?, ?, ?)
        """, (
            int(row["ID"]),
            row["Name"],
            int(row["Age"]),
            float(row["Marks"])
        ))

con.commit()

print("CSV data imported successfully")

con.close()