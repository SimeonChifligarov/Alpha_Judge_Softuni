# Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:
# ASCII_OFFSET = 97
#
# n_letters = int(input())
#
# for i in range(n_letters):
#     for j in range(n_letters):
#         for k in range(n_letters):
#             print(f'{chr(i + ASCII_OFFSET)}{chr(j + ASCII_OFFSET)}{chr(k + ASCII_OFFSET)}')
#

# Solution 2:
ASCII_OFFSET = 97

n_letters = int(input())

for i in range(ASCII_OFFSET, n_letters + ASCII_OFFSET):
    for j in range(ASCII_OFFSET, n_letters + ASCII_OFFSET):
        for k in range(ASCII_OFFSET, n_letters + ASCII_OFFSET):
            print(f'{chr(i)}{chr(j)}{chr(k)}')
