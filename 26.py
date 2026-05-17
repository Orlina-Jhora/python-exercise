print('---Count vowels and consonants-----')
text = input("Enter a string: ")
vowels = 0
consonants = 0
for x in text:

    if x in "aeiouAEIOU":
        vowels += 1

    elif x.isalpha():
        consonants += 1

print(f"Vowels = {vowels}")
print(f"Consonants = {consonants}")