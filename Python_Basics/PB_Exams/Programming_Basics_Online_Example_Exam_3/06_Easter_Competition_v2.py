def easter_bread_competition(bread_count):
    highest_score = 0
    best_baker = ''

    for _ in range(bread_count):
        baker_name = input()
        total_points = 0

        while True:
            command = input()
            if command == 'Stop':
                break
            points = int(command)
            total_points += points

        print(f'{baker_name} has {total_points} points.')
        if total_points > highest_score:
            highest_score = total_points
            best_baker = baker_name
            print(f'{baker_name} is the new number 1!')

    print(f'{best_baker} won competition with {highest_score} points!')


breads = int(input())
easter_bread_competition(breads)
