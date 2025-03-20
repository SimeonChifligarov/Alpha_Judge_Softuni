# The ban list should be entered on the first input line and the text on the second input line.

ban_list = input().split(', ')
text = input()

for banned_word in ban_list:
    text = text.replace(banned_word, '*' * len(banned_word))
print(text)
