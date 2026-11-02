# Handle database errors
import sqlite3

try:
    con = sqlite3.connect("student_db.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

except sqlite3.Error as e:
    print("Database Error:", e)

finally:
    if 'con' in locals():
        con.close()