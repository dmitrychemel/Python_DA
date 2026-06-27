text = "#Python for #DataAnalytics"

words = text.split()
hashgtags = []

for word in words:
    if word.startswith("#"):
        hashgtags.append(word)

print(hashgtags)