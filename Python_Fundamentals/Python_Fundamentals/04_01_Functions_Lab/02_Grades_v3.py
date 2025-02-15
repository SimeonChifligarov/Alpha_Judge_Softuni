def grade_to_word(grade: float) -> str:
    """
    Converts a numerical grade into a corresponding word description.
    """
    if 2.00 <= grade <= 2.99:
        return 'Fail'
    elif 3.00 <= grade <= 3.49:
        return 'Poor'
    elif 3.50 <= grade <= 4.49:
        return 'Good'
    elif 4.50 <= grade <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade <= 6.00:
        return 'Excellent'
    return 'Invalid Grade'


if __name__ == '__main__':
    user_grade = float(input())
    result = grade_to_word(grade=user_grade)
    print(result)
