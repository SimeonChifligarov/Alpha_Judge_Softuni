def is_valid_length(password: str) -> bool:
    return 6 <= len(password) <= 10


def is_alphanumeric(password: str) -> bool:
    return password.isalnum()


def has_at_least_two_digits(password: str) -> bool:
    return sum(char.isdigit() for char in password) >= 2


def validate_password(password: str) -> None:
    valid_length = is_valid_length(password)
    valid_chars = is_alphanumeric(password)
    valid_digits = has_at_least_two_digits(password)

    if valid_length and valid_chars and valid_digits:
        print('Password is valid')
    else:
        if not valid_length:
            print('Password must be between 6 and 10 characters')
        if not valid_chars:
            print('Password must consist only of letters and digits')
        if not valid_digits:
            print('Password must have at least 2 digits')


password_input = input()
validate_password(password_input)
