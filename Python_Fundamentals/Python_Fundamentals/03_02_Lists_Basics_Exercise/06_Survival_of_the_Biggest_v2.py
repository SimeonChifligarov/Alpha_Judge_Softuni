# Write a program that receives a list of integer numbers and a number n.
# The number n represents the amount of numbers to remove from the list.
# You should remove the smallest ones.
# Input
# On the first line you will receive a string (numbers separated by a space),
# on the second line you will receive a number n (count of numbers to remove).

list_of_integers = [int(num) for num in input().split()]
n = int(input())

for removed_num in range(n):
    list_of_integers.pop(list_of_integers.index(min(list_of_integers)))

print(*list_of_integers, sep=', ')
