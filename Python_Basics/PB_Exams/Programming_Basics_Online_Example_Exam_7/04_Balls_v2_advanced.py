def calculate_ball_points(colors):
    points = 0
    color_counts = {
        'red': 0,
        'orange': 0,
        'yellow': 0,
        'white': 0,
        'black': 0,
        'other': 0,
    }
    point_values = {
        'red': 5,
        'orange': 10,
        'yellow': 15,
        'white': 20,
    }
    black_divides = 0

    for color in colors:
        if color in point_values:
            points += point_values[color]
            color_counts[color] += 1
        elif color == 'black':
            points //= 2
            black_divides += 1
            color_counts['black'] += 1
        else:
            color_counts['other'] += 1

    result = (
        f'Total points: {points}',
        f'Red balls: {color_counts["red"]}',
        f'Orange balls: {color_counts["orange"]}',
        f'Yellow balls: {color_counts["yellow"]}',
        f'White balls: {color_counts["white"]}',
        f'Other colors picked: {color_counts["other"]}',
        f'Divides from black balls: {black_divides}',
    )
    return result


if __name__ == '__main__':
    ball_count_input = int(input())
    colors_input = [input() for _ in range(ball_count_input)]

    res = calculate_ball_points(colors=colors_input)
    print('\n'.join(res))
