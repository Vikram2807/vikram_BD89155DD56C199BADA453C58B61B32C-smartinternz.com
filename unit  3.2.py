class Student:

  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(students):
  sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)
  return sorted_students


# Example usage:
students = []
n = int(input("Enter the number of students: "))

for i in range(n):
  name = input("Enter the name of student {}: ".format(i + 1))
  roll_number = input("Enter the roll number of student {}: ".format(i + 1))
  cgpa = float(input("Enter the CGPA of student {}: ".format(i + 1)))
  student = Student(name, roll_number, cgpa)
  students.append(student)

sorted_students = sort_students(students)

print("Sorted students:")
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))
