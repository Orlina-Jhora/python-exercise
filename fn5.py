
def stats(numbers):

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for num in numbers:

        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

        total += num

    average = total / len(numbers)

    return {
        "min": smallest,
        "max": largest,
        "sum": total,
        "average": average
    }

numbers = []
count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print(stats(numbers))
