words = input().split()
searched_palindrome = input()

all_palindromes = [word for word in words if word == word[::-1]]
print(all_palindromes)
count = 0
for word in all_palindromes:
    if word == searched_palindrome:
        count += 1
print(f'Found palindrome {count} times')
