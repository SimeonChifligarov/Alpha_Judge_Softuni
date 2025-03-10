def create_food_dict(food_data: str) -> dict[str, int]:
    """Creates a dictionary from a space-separated string of food items and their quantities."""
    elements = food_data.split()
    return {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}


if __name__ == '__main__':
    food_input = input()
    food_dict = create_food_dict(food_data=food_input)
    print(food_dict)
