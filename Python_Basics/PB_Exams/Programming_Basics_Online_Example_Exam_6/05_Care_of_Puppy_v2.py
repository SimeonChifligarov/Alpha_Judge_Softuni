def puppy_food_check(initial_food_kg, food_eaten_list):
    total_food_grams = initial_food_kg * 1000
    total_eaten = sum(food_eaten_list)

    if total_eaten <= total_food_grams:
        return f'Food is enough! Leftovers: {total_food_grams - total_eaten} grams.'
    else:
        return f'Food is not enough. You need {total_eaten - total_food_grams} grams more.'


if __name__ == '__main__':
    initial_food_input = int(input())
    food_eaten_input = []
    while True:
        command = input()
        if command == 'Adopted':
            break
        food_eaten_input.append(int(command))

    result = puppy_food_check(initial_food_kg=initial_food_input, food_eaten_list=food_eaten_input)
    print(result)
