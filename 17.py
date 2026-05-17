print('---sum of digits of a number-----')
a = int(input("Enter a number: "))
sum = 0
while a > 0:
    digit = a % 10
    sum += digit
    a = a // 10
print(f"Sum = {sum}")