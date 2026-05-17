print('---Sum and average of 10 numbers----')
numbers = []
i = 0
while i < 10:
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    i += 1

sum = 0
i = 0

while i < 10:
    sum  += numbers[i]
    i += 1
average = sum / 10

print(f"Sum = {sum}")
print(f"Average = {average}")
