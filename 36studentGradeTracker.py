students = [
    {"name": "Brad Pitt", "grades" : [85, 90, 78]},
    {"name": "Angelina Jolie", "grades" : [92, 88, 95]},
    {"name": "Leonardo DiCaprio", "grades" : [76, 85, 80]}
]

def menu():
    print("\n" * 2)
    print("======================== STUDENT GRADE TRACKER ========================")
    print("-" * 60)
    print("1. Calculate Average Grade for a Student")
    print("2. Add New Student")
    print("3. Check Pass/Fail Status")
    print("4. Display All Students and Grades")
    print("5. Exit")
    print("-" * 60)

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def check_pass_fail(grades):
    average = calculate_average(grades)
    return "Pass" if average >= 40 else "Fail"    

def add_student(name, grades):
    students.append({"name": name, "grades": grades})    

def display_students():
    print("\n" * 2)
    print("List of Students and their Grades:")
    print("-" * 60)
    for student in students:
        avg = calculate_average(student['grades'])
        status = check_pass_fail(student['grades'])
        print(f"Name: {student['name']}")
        print(f"  Grades: {student['grades']}")
        print(f"  Average: {avg:.2f} | Status: {status}")
        print()

def find_student(search_name):
    for student in students:
        if student['name'].lower() == search_name.lower():
            return student
    return None

def get_student_average():
    search_name = input("Enter the name of the student: ")
    student = find_student(search_name)
    if student:
        avg = calculate_average(student['grades'])
        print(f"\nAverage grade for {student['name']}: {avg:.2f}")
    else:
        print("\nStudent not found in the database.")

def add_students():
    name = input("Enter the name of the new student: ")
    if find_student(name):
        print("\nStudent already exists in the database.")
        return
    grades_input = input("Enter the grades separated by commas: ")

    try:
        grades = [float(grade.strip()) for grade in grades_input.split(',') if grade.strip()]

        if any(grade < 0 or grade > 100 for grade in grades):
            print("\nGrades must be between 0 and 100.")
            return
        add_student(name, grades)
        print(f"\nStudent '{name}' added successfully.")
    except ValueError:
        print("\nInvalid input. Please enter numeric grades separated by commas.")

def get_pass_fail_status():
    search_name = input("Enter the name of the student: ")
    student = find_student(search_name)

    if student:
        avg = calculate_average(student['grades'])
        status = check_pass_fail(student['grades'])
        print(f"\n{student['name']} has {status}ed with an average grade of {avg:.2f}.")
    else:
        print("\nStudent not found in the database.")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            get_student_average()
            input("Press Enter to continue...")

        elif choice == '2':
            add_students()
            input("Press Enter to continue...")
            
        elif choice == '3':
            get_pass_fail_status()
            input("Press Enter to continue...")

        elif choice == '4':
            display_students()
            input("Press Enter to continue...")

        elif choice == '5':
            print("Exiting the Student Grade Tracker. Goodbye!")
            break

if __name__ == "__main__":
    main()



            
    

