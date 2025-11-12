class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B+"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C+"
        elif self.marks >= 40:
            return "C"
        else:
            return "NG"
        

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def get_average(self):
        if not self.subjects:
            return 0
        total = sum(subject.marks for subject in self.subjects)
        return total / len(self.subjects)
    
    def get_result(self):
        avg = self.get_average()
        if avg >= 40:
            return "PASS"
        else:
            return "FAIL"
        
    def print_report_card(self):
        print("\n" + "="*40)
        print("STUDENT REPORT CARD")
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Roll no.: {self.roll_no}")
        print("-" * 40)
        print(f"{'Subject' :<15} {'Marks':<10} {'Grade'}")
        print("-" * 40)

        for subject in self.subjects:
            print(f"{subject.name:<15} {subject.marks:<10} {subject.get_grade()}")

        print("-" *40)
        print(f"Average: {self.get_average():.2f}")
        print(f"Result: {self.get_result()}")
        print("=" * 40)

def main():

    student = Student("Ram Sharma", "12A-045")
    student.add_subject(Subject("Math", 85))
    student.add_subject(Subject("Science", 78))
    student.add_subject(Subject("English", 92))
    student.add_subject(Subject("Nepali", 88))
    student.add_subject(Subject("Social", 75))
    student.print_report_card()
    
    print("\n")
    student2 = Student("Sita Thapa", "12A-023")
    student2.add_subject(Subject("Math", 65))
    student2.add_subject(Subject("Science", 55))
    student2.add_subject(Subject("English", 70))
    student2.add_subject(Subject("Nepali", 60))
    student2.add_subject(Subject("Social", 58))
    student2.print_report_card()

if __name__ == "__main__":
    main()