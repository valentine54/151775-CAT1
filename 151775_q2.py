class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"{self.name}'s grades:")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, assignment_name, grade):
        student.add_assignment(assignment_name, grade)

    def display_students_grades(self):
        for student in self.students:
            student.display_grades()

# Interactive code example
if __name__ == "__main__":
    student1 = Student("Claire", "C-001")
    instructor = Instructor("Dr. Charlie", "Communications Skills")
    instructor.add_student(student1)
    instructor.assign_grade(student1, "Assignment 1", 85)
    instructor.display_students_grades()
