# Connect to SQLite database
import sqlite3

try:
    con = sqlite3.connect("student_db.db")
    print("Database connected successfully")
    con.close()

except sqlite3.Error as e:
    print("Database Error:", e)