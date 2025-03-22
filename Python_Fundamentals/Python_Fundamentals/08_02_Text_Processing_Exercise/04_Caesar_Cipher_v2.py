message = input()

new_char = ''
result = ''

for index in range(len(message)):
    char = message[index]
    new_char = chr(ord(char) + 3)
    result += new_char

print(result)
