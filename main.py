import json

# Initialize the student data storage
data_file = 'students.json'

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    students[student_id] = {'name': name, 'grades': []}
    print(f"Student {name} added.")
    save_data(students)

def record_grade(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        grade = float(input("Enter grade: "))
        students[student_id]['grades'].append(grade)
        print("Grade recorded.")
        save_data(students)
    else:
        print("Student not found.")

def view_grades(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        grades = students[student_id]['grades']
        print(f"Grades for {students[student_id]['name']}: {grades}")
    else:
        print("Student not found.")

def calculate_average(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        grades = students[student_id]['grades']
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade for {students[student_id]['name']}: {average:.2f}")
        else:
            print("No grades recorded.")
    else:
        print("Student not found.")

def main():
    students = load_data()

    while True:
        print("\n1. Add Student")
        print("2. Record Grade")
        print("3. View Grades")
        print("4. Calculate Average")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            record_grade(students)
        elif choice == '3':
            view_grades(students)
        elif choice == '4':
            calculate_average(students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
