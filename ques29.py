# Insert and fetch using functions
import sqlite3

def insert_data(name, age, marks):
    con = sqlite3.connect("student_db.db")
    cur = con.cursor()

    cur.execute("""
    INSERT INTO students(name, age, marks)
    VALUES (?, ?, ?)
    """, (name, age, marks))

    con.commit()
    con.close()

    print("Record inserted successfully")


def fetch_data():
    con = sqlite3.connect("student_db.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

    con.close()


insert_data("Rohit", 22, 92)

fetch_data()