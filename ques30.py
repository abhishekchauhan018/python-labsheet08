# Menu-driven student management system
import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

# Create students table
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks REAL
)
""")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        cur.execute("""
        INSERT INTO students(name, age, marks)
        VALUES (?, ?, ?)
        """, (name, age, marks))

        con.commit()
        print("Student added successfully")

    elif choice == "2":
        cur.execute("SELECT * FROM students")

        for row in cur.fetchall():
            print(row)

    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        marks = float(input("Enter new marks: "))

        cur.execute("""
        UPDATE students SET marks=?
        WHERE id=?
        """, (marks, student_id))

        con.commit()
        print("Student updated successfully")

    elif choice == "4":
        student_id = int(input("Enter student ID: "))

        cur.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        con.commit()
        print("Student deleted successfully")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")

con.close()