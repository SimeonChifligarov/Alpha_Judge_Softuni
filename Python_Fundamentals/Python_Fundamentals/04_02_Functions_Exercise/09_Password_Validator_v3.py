def validate_password(password: str) -> None:
    """
    Checks if the given password is valid based on defined rules and prints the validation messages.
    """
    errors = []

    if not (6 <= len(password) <= 10):
        errors.append('Password must be between 6 and 10 characters')

    if not password.isalnum():
        errors.append('Password must consist only of letters and digits')

    if sum(char.isdigit() for char in password) < 2:
        errors.append('Password must have at least 2 digits')

    if errors:
        print('\n'.join(errors))
    else:
        print('Password is valid')


if __name__ == '__main__':
    input_password = input()
    validate_password(password=input_password)
