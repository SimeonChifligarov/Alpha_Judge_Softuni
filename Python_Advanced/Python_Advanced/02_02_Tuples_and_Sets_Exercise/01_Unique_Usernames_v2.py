def collect_unique_usernames(total_count: int) -> set:
    """
    This function collects only unique usernames from given input.

    Args:
        total_count (int): The number of usernames to read

    Returns:
        set: A set containing only unique usernames
    """
    unique_usernames = {input() for _ in range(total_count)}
    return unique_usernames


if __name__ == '__main__':
    usernames_count_input = int(input())
    result_usernames = collect_unique_usernames(total_count=usernames_count_input)
    for username in result_usernames:
        print(username)
