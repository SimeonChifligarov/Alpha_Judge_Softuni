string = input()

all_digits = []
all_letters = []
all_others = []

for char in string:
    if char.isdigit():
        all_digits.append(char)
    elif char.isalpha():
        all_letters.append(char)
    # elif not char.isalnum():
    else:
        all_others.append(char)

for ll in (all_digits, all_letters, all_others):
    print(''.join(ll))

# print(''.join(all_digits))
# print(''.join(all_letters))
# print(''.join(all_others))
