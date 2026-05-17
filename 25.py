print('---Print all vowels from a given string-----')
text = input("Enter a string: ")
for x in text:
    if x in "aeiouAEIOU":
        print(x)