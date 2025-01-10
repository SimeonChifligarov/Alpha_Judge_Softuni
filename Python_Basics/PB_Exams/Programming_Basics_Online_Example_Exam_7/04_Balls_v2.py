def calculate_ball_points(colors):
    points = 0
    red_count = 0
    orange_count = 0
    yellow_count = 0
    white_count = 0
    black_divides = 0
    other_colors = 0

    for color in colors:
        if color == 'red':
            points += 5
            red_count += 1
        elif color == 'orange':
            points += 10
            orange_count += 1
        elif color == 'yellow':
            points += 15
            yellow_count += 1
        elif color == 'white':
            points += 20
            white_count += 1
        elif color == 'black':
            points //= 2
            black_divides += 1
        else:
            other_colors += 1

    result = (
        f'Total points: {points}',
        f'Red balls: {red_count}',
        f'Orange balls: {orange_count}',
        f'Yellow balls: {yellow_count}',
        f'White balls: {white_count}',
        f'Other colors picked: {other_colors}',
        f'Divides from black balls: {black_divides}',
    )
    return result


if __name__ == '__main__':
    ball_count_input = int(input())
    colors_input = [input() for _ in range(ball_count_input)]

    res = calculate_ball_points(colors=colors_input)
    print('\n'.join(res))
