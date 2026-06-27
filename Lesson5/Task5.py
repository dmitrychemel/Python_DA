text = input("Enter text:")
new_text = ""

for l in text:
    if l.isdigit():
        new_text += "*"
    else:
        new_text += l

print(new_text)
