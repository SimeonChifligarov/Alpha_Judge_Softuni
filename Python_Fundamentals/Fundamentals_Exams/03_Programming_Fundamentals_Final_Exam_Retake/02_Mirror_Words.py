import re

s = input()

matches = list(re.finditer(r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1', s))
if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

mirrors = []
for m in matches:
    a, b = m.group(2), m.group(3)
    if a == b[::-1]:
        mirrors.append(f"{a} <=> {b}")
if not mirrors:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirrors))
