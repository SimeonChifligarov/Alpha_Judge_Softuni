def is_walk_enough():
    walk_minutes = int(input())
    daily_walks = int(input())
    daily_calories = int(input())

    burned_calories = walk_minutes * daily_walks * 5
    required_burned = daily_calories * 0.50

    if burned_calories >= required_burned:
        print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
    else:
        print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')


if __name__ == '__main__':
    is_walk_enough()
