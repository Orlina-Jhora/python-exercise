print('---Factorial of a number-----')
a = int(input("Enter a number: "))
i = 1
fact = 1
while i <= a:
    fact *= i
    i += 1
print(f"Factorial = {fact}")