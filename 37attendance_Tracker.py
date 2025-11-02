attendance = {
    "Brad Pitt" : ["P", "A", "P", "P", "A"],
    "Angelina Jolie" : ["P", "P", "P", "P", "P"],   
    "Leonardo DiCaprio" : ["A", "A", "P", "A", "P"]
}

THRESHOLD = 75.0

def menu():
    print("\n" + "=" * 72)
    print("======= ATTENDANCE TRACKER MENU =======")
    print("=" * 72)
    print("1. Mark Today's Attendance")
    print("2. View Student Attendance Stats")
    print("3. View All Students' Attendance Stats")
    print("4. Add New Student")
    print("5. Remove Student")
    print("6. Exit")
    print("=" * 72)
    print("\n")

# ================= CALCULATION LAYER ================

def calculate_percentage(attendance_list):
    if not attendance_list:
        return 0.0
    present_count = attendance_list.count("P")
    total_days = len(attendance_list)
    return (present_count / total_days) * 100

def is_at_risk(percentage, threshold = THRESHOLD):
    return percentage < threshold

# ================= DATA LAYER =======================

def find_student(name):
    for student_name in attendance.keys():
        if student_name.lower() ==  name.lower():
            return student_name
    return None

def mark_attendance(name, status):
    if name in attendance:
        attendance[name].append(status)
    else:
        attendance[name] = [status]

def get_student_stats(name):
    if name not in attendance:
        return None
    
    record = attendance[name]
    percentage = calculate_percentage(record)
    at_risk = is_at_risk(percentage)
    present = record.count("P")
    absent = record.count("A")
    total = len(record)
    return {
        "name": name,
        "record": record,
        "present": present,
        "absent": absent,
        "total": total,
        "percentage": percentage,
        "at_risk": at_risk
    }

# ==================== REPORT LAYER ====================

def mark_today_attendance():
    print("\n" + "=" * 72)
    print("MARK TODAY'S ATTENDANCE")
    print("=" * 72)

    if not attendance:
        print("No students found. Please add students first.")
        return

    for student_name in attendance.keys():
        while True:
            status = input(f"Is {student_name} present? (P/A): ").strip().upper()
            if status in ["P", "A"]:
                mark_attendance(student_name, status)
                break
            else:
                print("Invalid input. Please enter 'P' for Present or 'A' for Absent.") 
    print("Today's attendance has been marked successfully.")

def view_student_stats():
    search_name = input("Enter the student's name: ")
    actual_name = find_student(search_name)
    if not actual_name:
        print(f"Studetn '{search_name}' not found. ")
        return

    stats = get_student_stats(actual_name)
    print("\n" + "=" * 72)
    print(f"ATTENDANCE REPORT FOR {stats['name'].upper()}")
    print("=" * 72)
    print(f"Total Days:        {stats['total']}")
    print(f"Present:           {stats['present']} days")
    print(f"Absent:            {stats['absent']} days")
    print(f"Attendance %:      {stats['percentage']:.2f}%")
    print(f"Status:            {'AT RISK' if stats['at_risk'] else 'SAFE'}")
    print(f"Record:            {' '.join(stats['record'])}")
    print("=" * 72)

def view_all_reports():
    print("\n" + "=" * 72)
    print("ALL STUDENTS' ATTENDANCE REPORT")
    print("=" * 72)

    if not attendance:
        print("No students found. Please add students first.")
        return

    for student_name in attendance.keys():
        stats = get_student_stats(student_name)
        print(f"\nStudent: {stats['name']}")
        print(f"Total Days:        {stats['total']}")
        print(f"Present:           {stats['present']} days")
        print(f"Absent:            {stats['absent']} days")
        print(f"Attendance %:      {stats['percentage']:.2f}%")
        print(f"Status:            {'AT RISK' if stats['at_risk'] else 'SAFE'}")
        print(f"Record:            {' '.join(stats['record'])}")
        print("-" * 72)

def add_new_student():
    print("\n" + "=" * 72)
    name = input("Enter the new student's name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    if find_student(name):
        print(f"Student '{name}' already exists.")
        return
    
    attendance[name] = []
    print(f"Student '{name}' has been added successfully.")

def view_at_risk_students():
    print("\n" + "=" * 72)
    print(f"STUDENTS AT RISK (Attendance below {THRESHOLD}%)")
    print("=" * 72)

    at_risk_found = False
    for student_name in attendance.keys():
        stats = get_student_stats(student_name)
        if stats['at_risk']:
            at_risk_found = True
            print(f"\n {stats['name']}")
            print(f"Attendance : {stats['percentage']:.2f}%"
                  f" | Present: {stats['present']}/{stats['total']} days")
            print(f"Needs {int((THRESHOLD/100)*stats['total'] - stats['present']) + 1} more present days to be safe.")

        if not at_risk_found:
            print("No students are currently at risk.")

        print("\n" + "=" * 72)

def main():
    while True:
        menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            mark_today_attendance()
            input("Press Enter to continue...")
        elif choice == '2':
            view_student_stats()
            input("Press Enter to continue...")
        elif choice == '3':
            view_all_reports()
            input("Press Enter to continue...")
        elif choice == '4':
            add_new_student()
            input("Press Enter to continue...")
        elif choice == '5':
            view_at_risk_students()
            input("Press Enter to continue...")
        elif choice == '6':
            print("Exiting Attendance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()


 


