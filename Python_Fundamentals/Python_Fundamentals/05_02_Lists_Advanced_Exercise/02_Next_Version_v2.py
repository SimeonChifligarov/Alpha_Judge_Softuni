def increment_version(version: str) -> str:
    """Increments a dot-separated version string."""
    version_number = int(''.join(version.split('.'))) + 1
    return '.'.join(map(str, str(version_number)))


if __name__ == '__main__':
    previous_version = input()
    print(increment_version(previous_version))
