list_of_chars = input().split(', ')

chars_and_ascii_dict = {}
for ch in list_of_chars:
    # if ch not in chars_and_ascii_dict:
    #     chars_and_ascii_dict[ch] = ord(ch)
    chars_and_ascii_dict[ch] = ord(ch)

print(chars_and_ascii_dict)
