text = input("Enter a sentence: ")

def word_count(text):

    text = text.lower()

    punctuation = ".,!?;:"
    for mark in punctuation:
        text = text.replace(mark, "")
  
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(text))
