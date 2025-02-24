def remove_vowels(text: str) -> str:
    """Removes vowels from the given text."""
    vowels = {'a', 'e', 'i', 'o', 'u'}  # set for faster lookup
    return ''.join(char for char in text if char.lower() not in vowels)


def main():
    received_text = input()
    print(remove_vowels(received_text))


if __name__ == '__main__':
    main()
