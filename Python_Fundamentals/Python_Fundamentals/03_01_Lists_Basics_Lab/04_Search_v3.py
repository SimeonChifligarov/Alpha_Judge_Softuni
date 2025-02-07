# You will receive a number n and a word. On the next n lines you will be given some strings.
# You have to add them in a list and print them. After that you have to filter out only the strings
# that include the given word and print that list too.

number = int(input())
word = input()

all_strings = [input() for _ in range(number)]
print(all_strings)

filtered_strings = [words for words in all_strings if word in words]
print(filtered_strings)
