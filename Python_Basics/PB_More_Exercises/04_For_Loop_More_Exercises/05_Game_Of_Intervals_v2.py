moves = int(input())
numbers = [int(input()) for _ in range(moves)]

result = 0
count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
count_invalid = 0

for number in numbers:
    if 0 <= number <= 9:
        result += 0.2 * number
        count_0_9 += 1
    elif 10 <= number <= 19:
        result += 0.3 * number
        count_10_19 += 1
    elif 20 <= number <= 29:
        result += 0.4 * number
        count_20_29 += 1
    elif 30 <= number <= 39:
        result += 50
        count_30_39 += 1
    elif 40 <= number <= 50:
        result += 100
        count_40_50 += 1
    else:
        result /= 2
        count_invalid += 1

total_numbers = moves
percent_0_9 = (count_0_9 / total_numbers) * 100
percent_10_19 = (count_10_19 / total_numbers) * 100
percent_20_29 = (count_20_29 / total_numbers) * 100
percent_30_39 = (count_30_39 / total_numbers) * 100
percent_40_50 = (count_40_50 / total_numbers) * 100
percent_invalid = (count_invalid / total_numbers) * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {percent_0_9:.2f}%')
print(f'From 10 to 19: {percent_10_19:.2f}%')
print(f'From 20 to 29: {percent_20_29:.2f}%')
print(f'From 30 to 39: {percent_30_39:.2f}%')
print(f'From 40 to 50: {percent_40_50:.2f}%')
print(f'Invalid numbers: {percent_invalid:.2f}%')
