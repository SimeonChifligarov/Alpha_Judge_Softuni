class vowels:
    """
    This class represents an iterator over the vowels in a string,
    skipping any non-letter characters and matching vowels case-insensitively.

    Args:
        text (str): The input string to filter vowels from.
    """

    def __init__(self, text: str) -> None:
        self.text = text
        self.vowels = 'aeiouy'
        self.index = 0

    def __iter__(self) -> 'vowels':
        return self

    def __next__(self) -> str:
        while self.index < len(self.text):
            current_char = self.text[self.index]
            self.index += 1
            if current_char.isalpha() and current_char.lower() in self.vowels:
                return current_char
        raise StopIteration


if __name__ == '__main__':
    # my_string = vowels(text='Abcedifuty0o!!!@#123')
    # for char in my_string:
    #     print(char)
    pass
