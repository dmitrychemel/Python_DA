text = input("Enter text: ")

words = text.split()
word_max = words[0]

for el in words:
    if len(el) > len(word_max):
        word_max = el

print(word_max)
