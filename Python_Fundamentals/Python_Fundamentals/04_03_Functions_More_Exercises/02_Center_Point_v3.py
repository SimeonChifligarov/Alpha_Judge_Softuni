import math


def closest_point(x_1: float, y_1: float, x_2: float, y_2: float) -> str:
    """
    Determines which of the two points (x_1, y_1) or (x_2, y_2)
    is closer to the origin (0, 0), rounding down coordinates.

    :param x_1: X-coordinate of the first point.
    :param y_1: Y-coordinate of the first point.
    :param x_2: X-coordinate of the second point.
    :param y_2: Y-coordinate of the second point.
    :return: The closest point as a formatted string "(X, Y)".
    """
    distance_1 = math.sqrt(x_1 ** 2 + y_1 ** 2)
    distance_2 = math.sqrt(x_2 ** 2 + y_2 ** 2)

    if distance_1 <= distance_2:
        return f'({math.floor(x_1)}, {math.floor(y_1)})'
    return f'({math.floor(x_2)}, {math.floor(y_2)})'


if __name__ == '__main__':
    x1_input = float(input())
    y1_input = float(input())
    x2_input = float(input())
    y2_input = float(input())

    result = closest_point(x_1=x1_input, y_1=y1_input, x_2=x2_input, y_2=y2_input)
    print(result)
