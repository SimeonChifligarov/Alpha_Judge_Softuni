string = input()

for index in range(len(string) - 1, 0, -1):
    if string[index] == string[index - 1]:
        string = string[:index - 1] + string[index:]

print(string)
