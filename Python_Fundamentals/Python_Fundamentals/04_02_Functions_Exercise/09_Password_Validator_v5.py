def is_length_valid(password: str) -> bool:
    """
    Checks if the password length is between 6 and 10 characters.
    """
    return 6 <= len(password) <= 10


def is_alphanumeric(password: str) -> bool:
    """
    Checks if the password consists only of letters and digits.
    """
    return password.isalnum()


def has_minimum_digits(password: str) -> bool:
    """
    Checks if the password contains at least 2 digits.
    """
    return sum(char.isdigit() for char in password) >= 2


def validate_password(password: str) -> list[str]:
    """
    Validates the given password using helper functions and returns validation messages.
    """
    errors = []

    if not is_length_valid(password):
        errors.append('Password must be between 6 and 10 characters')

    if not is_alphanumeric(password):
        errors.append('Password must consist only of letters and digits')

    if not has_minimum_digits(password):
        errors.append('Password must have at least 2 digits')

    return errors if errors else ['Password is valid']


if __name__ == '__main__':
    input_password = input()
    result = validate_password(password=input_password)
    print('\n'.join(result))
