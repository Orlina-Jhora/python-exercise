print('---Average marks of 5 students----')
i = 1
total = 0

while i <= 5:
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    total += marks
    i += 1

average = total / 5

print("Average marks =", average)