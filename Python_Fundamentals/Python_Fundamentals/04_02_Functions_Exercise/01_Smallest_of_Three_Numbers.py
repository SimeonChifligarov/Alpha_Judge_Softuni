def min_of_three(num_1, num_2, num_3):
    if num_1 <= num_2 and num_1 <= num_3:
        return num_1
    elif num_2 <= num_1 and num_2 <= num_3:
        return num_2
    else:
        return num_3


a = int(input())
b = int(input())
c = int(input())
print(min_of_three(a, b, c))
