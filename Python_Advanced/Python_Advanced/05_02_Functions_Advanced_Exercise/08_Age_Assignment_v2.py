def age_assignment(*people: str, **age_map: int) -> str:
    """
    This function matches names to ages using their first letters.

    Args:
        people: Names of people
        age_map: Mapping of letters to ages

    Returns:
        A string with each name and its age
    """
    assigned_ages = {}
    for person in people:
        assigned_ages[person] = age_map[person[0]]
    sorted_result = sorted(assigned_ages.items(), key=lambda x: x[0])
    output = [f'{name} is {age} years old.' for name, age in sorted_result]
    return '\n'.join(output)

# if __name__ == '__main__':
#     input_people = ('Daisy', 'Aaron', 'Ben')
#     input_ages = {
#         'A': 22,
#         'B': 27,
#         'D': 19
#     }
#     print(age_assignment(*input_people, **input_ages))
