start = int(input())
end = int(input())

for number in range(start, end + 1):
    num_str = str(number)

    even_sum = 0
    odd_sum = 0

    for i in range(len(num_str)):
        if i % 2 == 0:
            even_sum += int(num_str[i])
        else:
            odd_sum += int(num_str[i])

    if even_sum == odd_sum:
        print(number, end=' ')
