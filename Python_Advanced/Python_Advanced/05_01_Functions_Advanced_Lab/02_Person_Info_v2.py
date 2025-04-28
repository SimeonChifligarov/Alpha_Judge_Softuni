def get_info(name: str, age: int, town: str) -> str:
    """
    This function makes a sentence about a person using name, age and town.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.
        town (str): The town where the person lives.

    Returns:
        str: A full sentence with the person's information.
    """
    result = f'This is {name} from {town} and he is {age} years old'
    return result

# if __name__ == '__main__':
#     person_data = {
#         'name': input(),
#         'age': int(input()),
#         'town': input(),
#     }
#     info_result = get_info(**person_data)
#     print(info_result)
