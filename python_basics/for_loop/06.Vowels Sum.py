text = input()
total_vowels = 0

for ch in text:

    if ch == 'a':
        total_vowels += 1
    if ch == 'e':
        total_vowels += 2
    if ch == 'i':
        total_vowels += 3
    if ch == 'o':
        total_vowels += 4
    if ch == 'u':
        total_vowels += 5

print(total_vowels)
