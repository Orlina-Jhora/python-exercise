print('---Largest number from list of 10 numbers-----')
numbers = []
i = 0
while i < 10:
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    i += 1
largest = numbers[0]

i = 0
while i < 10:
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print(f"Largest number = {largest}")