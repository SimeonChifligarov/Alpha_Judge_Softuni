def get_next_version(version: str) -> str:
    """
    Returns the next version string based on the given version format "n1.n2.n3".
    """
    parts = [int(num) for num in version.split('.')]
    parts[2] += 1

    for i in range(2, 0, -1):
        if parts[i] > 9:
            parts[i] = 0
            parts[i - 1] += 1

    return '.'.join(map(str, parts))


if __name__ == '__main__':
    version_input = input()
    next_version = get_next_version(version=version_input)
    print(next_version)
