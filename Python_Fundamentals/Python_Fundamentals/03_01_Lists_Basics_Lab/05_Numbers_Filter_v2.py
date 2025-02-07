# You will receive a single number n. On the next n lines you will receive integers.
# After that you will be given one of the following commands:

number = int(input())

list_of_numbers = [int(input()) for _ in range(number)]

command = input()  # even, odd, negative, or positive
if command == 'even':
    list_of_filtered = [num for num in list_of_numbers if num % 2 == 0]
elif command == 'odd':
    list_of_filtered = [num for num in list_of_numbers if num % 2 != 0]
elif command == 'negative':
    list_of_filtered = [num for num in list_of_numbers if num < 0]
elif command == 'positive':
    list_of_filtered = [num for num in list_of_numbers if num >= 0]
else:  # handle invalid input?
    list_of_filtered = []

print(list_of_filtered)
