def is_valid_username(username: str) -> bool:
    """
    Checks if the given username is valid.
    A valid username:
    - Has a length between 3 and 16 characters inclusive
    - Contains only letters, numbers, hyphens, and underscores
    - Has no redundant symbols before, after, or in between
    """
    return 3 <= len(username) <= 16 and username.replace('-', '').replace('_', '').isalnum()


def filter_valid_usernames(usernames: str) -> list[str]:
    """
    Filters and returns a list of valid usernames from the given input string.
    """
    return [username for username in usernames.split(', ') if is_valid_username(username)]


if __name__ == '__main__':
    usernames_input: str = input()
    valid_usernames: list[str] = filter_valid_usernames(usernames=usernames_input)
    print('\n'.join(valid_usernames))
