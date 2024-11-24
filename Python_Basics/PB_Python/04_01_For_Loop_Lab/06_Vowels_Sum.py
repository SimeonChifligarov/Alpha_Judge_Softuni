text = input()

vowel_values = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5,
}

total_sum = sum(vowel_values[char] for char in text if char in vowel_values)

print(total_sum)
