a = int(input())
b = int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')

c = b
b = a
a = c

print('After:')
print(f'a = {a}')
print(f'b = {b}')
