text_as_list = list(input())
stack = []

for i in range(len(text_as_list)):
    stack.append(text_as_list.pop())

print(''.join(stack))
