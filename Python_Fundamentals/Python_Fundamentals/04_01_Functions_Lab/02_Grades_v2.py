def grade_to_words(grade):
    grade_dict = {
        (2.00, 2.99): 'Fail',
        (3.00, 3.49): 'Poor',
        (3.50, 4.49): 'Good',
        (4.50, 5.49): 'Very Good',
        (5.50, 6.00): 'Excellent'
    }

    for (low, high), word in grade_dict.items():
        if low <= grade <= high:
            return word

    return


grade_data = float(input())
print(grade_to_words(grade_data))
