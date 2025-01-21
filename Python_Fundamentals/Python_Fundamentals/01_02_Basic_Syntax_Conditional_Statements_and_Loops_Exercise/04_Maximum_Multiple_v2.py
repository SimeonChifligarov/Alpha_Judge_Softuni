divisor = int(input())
bound = int(input())

current_number = bound

while not current_number % divisor == 0:
    current_number -= 1

print(current_number)
