# Write a program that receives two numbers (factor and count) and creates a list with length
# of the given count and contains only elements that are multiples of the given factor.

factor = int(input())
count = int(input())

list_of_factors = []
for i in range(1, count + 1):
    current_number = i * factor
    list_of_factors.append(current_number)
print(list_of_factors)
