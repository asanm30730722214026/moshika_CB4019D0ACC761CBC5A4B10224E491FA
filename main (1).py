class Student:
  
  def __init__(self, name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  #sort the list of student in descending order of cgpa
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students
  #exaple usage:
student = [
    Student("moshi","A123",9.7),
    Student("savithiri","A124",9.8),
    Student("kathir","A125",9.8),
    Student("valar","A126",9.9),
]
sorted_students = sort_students(student)
#print the sorted list of students
for student in sorted_students:
  print("Name: {},Roll Number: {},CGPA:{}".format(student.name,student.roll_number,student.cgpa))