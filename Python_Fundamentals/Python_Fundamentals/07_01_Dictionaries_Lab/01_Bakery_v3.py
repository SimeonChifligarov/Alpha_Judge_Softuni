def create_food_dict(food_items: list[str]) -> dict[str, int]:
    """Creates a dictionary from a list of food items and their quantities."""
    return {food_items[i]: int(food_items[i + 1]) for i in range(0, len(food_items), 2)}


if __name__ == '__main__':
    food_input = input().split()
    food_dict = create_food_dict(food_items=food_input)
    print(food_dict)
