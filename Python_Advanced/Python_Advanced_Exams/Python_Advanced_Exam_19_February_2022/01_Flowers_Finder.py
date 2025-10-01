from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = {"rose": set("rose"),
         "tulip": set("tulip"),
         "lotus": set("lotus"),
         "daffodil": set("daffodil")}

found = {word: set() for word in words}
word_found = None

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    for word, letters in words.items():
        if v in letters:
            found[word].add(v)
        if c in letters:
            found[word].add(c)
        if found[word] == letters:
            word_found = word
            break
    if word_found:
        break

if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print("Vowels left: " + " ".join(vowels))
if consonants:
    print("Consonants left: " + " ".join(consonants))
