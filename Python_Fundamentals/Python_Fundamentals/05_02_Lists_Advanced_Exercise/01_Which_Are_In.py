# Given two lists of strings print a new list of the strings that contains words
# from the first list which are substrings of any of the strings in the second list
# (only unique values)

first_string_list = input().split(', ')
second_string_list = input().split(', ')

repetition_list = [substring for word in second_string_list for substring in first_string_list if substring in word]

print(sorted(set(repetition_list), key=first_string_list.index))
