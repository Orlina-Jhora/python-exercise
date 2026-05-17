print('---Smallert number from list of 10 numbers-----')
numbers = []
i = 0
while i < 10:
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    i += 1
smallest = numbers[0]

i = 0
while i < 10:
    if numbers[i] < smallest:
        smallest = numbers[i]
    i += 1
print(f"Smallest number = {smallest}")