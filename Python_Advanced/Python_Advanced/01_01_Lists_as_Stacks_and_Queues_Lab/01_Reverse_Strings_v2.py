text = input()
stack = []

for i in range(len(text)):
    stack.append(text[-i - 1])

print(''.join(stack))
