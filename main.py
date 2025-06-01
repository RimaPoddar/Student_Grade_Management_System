import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS students 
                (
                    student_id TEXT PRIMARY KEY ,
                    name TEXT
                )'''
              )

cursor.execute('''
                CREATE TABLE IF NOT EXISTS grades 
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id TEXT,
                    grade REAL,
                    FOREIGN KEY(student_id) REFERENCES students(student_id)
                )'''
            )


def add_student():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    try:
        cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (student_id, name))
        conn.commit()
        print(f"Student {name} added.")
    except sqlite3.IntegrityError:
        print("Student ID already exists.")

    conn.close()


def record_grade():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    
    if cursor.fetchone():
        grade = float(input("Enter grade: "))
        cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (student_id, grade))
        conn.commit()
        print("Grade recorded.")
    else:
        print("Student not found.")

    conn.close()


def view_grades():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    cursor.execute("SELECT name FROM students WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()

    if result:
        name = result[0]
        cursor.execute("SELECT grade FROM grades WHERE student_id = ?", (student_id,))
        grades = [row[0] for row in cursor.fetchall()]
        print(f"Grades for {name}: {grades}")
    else:
        print("Student not found.")

    conn.close()


def calculate_average():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    cursor.execute("SELECT name FROM students WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()

    if result:
        name = result[0]
        cursor.execute("SELECT grade FROM grades WHERE student_id = ?", (student_id,))
        grades = [row[0] for row in cursor.fetchall()]

        if grades:
            avg = sum(grades) / len(grades)
            print(f"Average grade for {name}: {avg:.2f}")
        else:
            print("No grades recorded.")
    else:
        print("Student not found.")

    conn.close()

def main():

    while True:
        print("\n1. Add Student")
        print("2. Record Grade")
        print("3. View Grades")
        print("4. Calculate Average")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            record_grade()
        elif choice == '3':
            view_grades()
        elif choice == '4':
            calculate_average()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
