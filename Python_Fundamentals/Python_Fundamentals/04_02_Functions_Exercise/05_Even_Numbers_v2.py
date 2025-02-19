nums = [int(el) for el in input().split()]
even_numbers = filter(lambda num: num % 2 == 0, nums)
print(list(even_numbers))
