ban_list = input().split(', ')
text = input()

for banned_word in ban_list:
    while banned_word in text:
        text = text.replace(banned_word, '*' * len(banned_word))
print(text)
