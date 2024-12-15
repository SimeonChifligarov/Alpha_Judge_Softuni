def password_generator(a, b, max_passwords):
    A = 35
    B = 64
    passwords = []
    count = 0

    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if count >= max_passwords:
                return passwords

            password = f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}'
            passwords.append(password)
            count += 1

            A += 1
            B += 1

            if A > 55:
                A = 35
            if B > 96:
                B = 64

    return passwords


a1 = int(input())
b1 = int(input())
max_passwords1 = int(input())

pass_words = password_generator(a=a1, b=b1, max_passwords=max_passwords1)
print('|'.join(pass_words), end='|')
