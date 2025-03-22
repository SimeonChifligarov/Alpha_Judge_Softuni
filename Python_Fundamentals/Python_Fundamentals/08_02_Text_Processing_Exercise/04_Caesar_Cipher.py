message = input()

result = ''
for char in message:
    new_char = chr(ord(char) + 3)
    result += new_char

print(result)
