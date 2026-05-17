print('---Reverse a string-----')
text = input("Enter a string: ")
reverse = ""
for x in text:
    reverse = x + reverse
print(f"Reverse = {reverse}")
