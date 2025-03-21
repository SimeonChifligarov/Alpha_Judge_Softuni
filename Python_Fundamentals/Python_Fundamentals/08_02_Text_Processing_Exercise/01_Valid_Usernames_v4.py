def is_valid_length(username: str) -> bool:
    """
    Checks if the username length is between 3 and 16 characters inclusive.
    """
    return 3 <= len(username) <= 16


def contains_valid_characters(username: str) -> bool:
    """
    Checks if the username contains only letters, numbers, hyphens, and underscores.
    """
    return username.replace('-', '').replace('_', '').isalnum()


def is_valid_username(username: str) -> bool:
    """
    Combines the length and character checks to determine if the username is valid.
    """
    return is_valid_length(username) and contains_valid_characters(username)


def filter_valid_usernames(usernames: str) -> list[str]:
    """
    Filters and returns a list of valid usernames from the given input string.
    """
    return [username for username in usernames.split(', ') if is_valid_username(username)]


if __name__ == '__main__':
    usernames_input: str = input()
    valid_usernames: list[str] = filter_valid_usernames(usernames=usernames_input)
    print('\n'.join(valid_usernames))
