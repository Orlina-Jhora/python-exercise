print('---Count words in a sentence----')
sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    count += 1

print(f"Total words ={count}")