def print_stars(n):
    if n == 0:
        return
    print('*' * n)
    print_stars(n - 1)


def print_hashes(n, max_n):
    if n > max_n:
        return
    print('#' * n)
    print_hashes(n + 1, max_n)


input_level = int(input())
print_stars(input_level)
print_hashes(1, input_level)
