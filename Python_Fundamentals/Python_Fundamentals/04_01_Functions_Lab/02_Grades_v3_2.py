def grade_to_word(grade: float) -> str:
    """
    Converts a numerical grade into a corresponding word description.
    """
    result = 'Invalid Grade'
    if 2.00 <= grade <= 2.99:
        result = 'Fail'
    elif 3.00 <= grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= grade <= 4.49:
        result = 'Good'
    elif 4.50 <= grade <= 5.49:
        result = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        result = 'Excellent'
    return result


if __name__ == '__main__':
    user_grade = float(input())
    res = grade_to_word(grade=user_grade)
    print(res)
