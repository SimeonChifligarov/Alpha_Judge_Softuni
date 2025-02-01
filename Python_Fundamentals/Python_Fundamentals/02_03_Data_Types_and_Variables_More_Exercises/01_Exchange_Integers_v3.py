a = int(input())
b = int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')

# c = b
# b = a
# a = c
# Pythonic way:
a, b = b, a

print('After:')
print(f'a = {a}')
print(f'b = {b}')
