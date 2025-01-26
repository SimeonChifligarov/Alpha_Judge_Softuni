def count_beach_words(text):
    words = ['sand', 'water', 'fish', 'sun']
    text_lower = text.lower()
    total_count = sum(text_lower.count(word) for word in words)
    return total_count


if __name__ == '__main__':
    input_text = input()
    result = count_beach_words(text=input_text)
    print(result)
