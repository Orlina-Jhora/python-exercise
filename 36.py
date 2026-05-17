print('---Count numbers greater than 50----')
numbers = []
i = 0
while i < 10:
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    i += 1

count = 0
i = 0

while i < 10:
    if numbers[i] > 50:
        count += 1
    i += 1

print(f"Numbers greater than 50 = {count}")