#1.Variable Swap
a = 10
b = 20

print("Before swapping:")
print(f"a = {a}")
print(f"b = {b}")

print("After swapping:")
print(f"a = {b}" )
print(f"b = {a}")

# 2. FizzBuzz

i = 1

while i <= 30:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    i += 1

# 3. Grade Calculator

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(get_grade(85))  
print(get_grade(55)) 
print(get_grade(40)) 

# 4. Even Numbers Sum

total = 0

for num in range(0, 101, 2):
    total += num

print(f"Sum of even numbers from 1 to 100 is: {total}")

# 5. Factorial Function

def factorial(n):
    result = 1

    while n > 0:
        result *= n
        n -= 1

    return result

print(factorial(5))  
print(factorial(0)) 