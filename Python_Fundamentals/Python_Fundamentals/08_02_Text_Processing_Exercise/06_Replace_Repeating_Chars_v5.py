def remove_consecutive_duplicates(text: str) -> str:
    """Removes consecutive duplicate letters from a string."""
    return ''.join(text[i] for i in range(len(text)) if i == 0 or text[i] != text[i - 1])


if __name__ == '__main__':
    input_text = input()
    result_text = remove_consecutive_duplicates(text=input_text)
    print(result_text)
