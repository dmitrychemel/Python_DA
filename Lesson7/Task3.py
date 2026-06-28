Text = input("Insert your text: ")
alfabet = {}

for letter in Text:
    if letter in alfabet:
        alfabet[letter] += 1
    else:
        alfabet[letter] = 1

print (alfabet)