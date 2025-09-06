import re

text = input()

threshold = 1
for ch in text:
    if ch.isdigit():
        threshold *= int(ch)

print(f"Cool threshold: {threshold}")

matches = re.findall(r'(::|\*\*)([A-Z][a-z]{2,})\1', text)
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for sep, word in matches:
    if sum(ord(c) for c in word) > threshold:
        print(f"{sep}{word}{sep}")
