# The input will be on two lines:
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you receive quantities of water, which you have to pour in the tank

CAPACITY = 255

number_of_lines = int(input())

current_water = 0
for pour in range(number_of_lines):
    water = int(input())
    current_water += water
    if current_water > CAPACITY:
        print('Insufficient capacity!')
        current_water -= water

print(current_water)
