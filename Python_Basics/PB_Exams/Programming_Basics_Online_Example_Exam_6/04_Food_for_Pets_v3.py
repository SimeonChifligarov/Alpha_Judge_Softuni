def pet_food_statistics(total_food, daily_food_data):
    total_eaten_dog = 0
    total_eaten_cat = 0
    total_biscuits = 0

    for day, (dog_food, cat_food) in enumerate(daily_food_data, start=1):
        total_eaten_dog += dog_food
        total_eaten_cat += cat_food
        daily_total = dog_food + cat_food

        if day % 3 == 0:
            total_biscuits += daily_total * 0.10

    total_eaten_food = total_eaten_dog + total_eaten_cat
    percent_eaten_food = (total_eaten_food / total_food) * 100
    percent_eaten_dog = (total_eaten_dog / total_eaten_food) * 100
    percent_eaten_cat = (total_eaten_cat / total_eaten_food) * 100

    return (
        f'Total eaten biscuits: {round(total_biscuits)}gr.',
        f'{percent_eaten_food:.2f}% of the food has been eaten.',
        f'{percent_eaten_dog:.2f}% eaten from the dog.',
        f'{percent_eaten_cat:.2f}% eaten from the cat.',
    )


if __name__ == '__main__':
    days_input = int(input())
    total_food_input = float(input())
    daily_food_input = [
        (int(input()), int(input())) for _ in range(days_input)
    ]
    result = pet_food_statistics(total_food=total_food_input, daily_food_data=daily_food_input)
    print('\n'.join(result))
