print('---Dictionary of 5 students (name: marks)----')
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

for name in students:
    print(name, ":", students[name])