# Create database
import sqlite3

con = sqlite3.connect("student_db.db")

print("Database created successfully")

con.close()