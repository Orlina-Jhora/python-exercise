print('---Separate even and odd numbers----')
numbers = []

i = 0
while i < 10:
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    i += 1

even = []
odd = []

i = 0
while i < 10:
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
    i += 1

print(f"Even numbers: {even}" )
print(f"Odd numbers: {odd}")