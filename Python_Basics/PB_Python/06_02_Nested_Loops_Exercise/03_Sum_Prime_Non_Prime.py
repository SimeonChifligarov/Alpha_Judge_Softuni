def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_sum = 0
non_prime_sum = 0

while True:
    user_input = input()

    if user_input == 'stop':
        break

    try:
        number = int(user_input)

        if number < 0:
            print('Number is negative.')
            continue

        if is_prime(number):
            prime_sum += number
        else:
            non_prime_sum += number

    except ValueError:
        continue

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
