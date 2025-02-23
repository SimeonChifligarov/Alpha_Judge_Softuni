import math


def closest_point(x_1: float, y_1: float, x_2: float, y_2: float) -> tuple[float, float, float, float]:
    """
    Determines the order of the two points (x_1, y_1) and (x_2, y_2)
    such that the point closest to the origin (0,0) comes first.

    :param x_1: X-coordinate of the first point.
    :param y_1: Y-coordinate of the first point.
    :param x_2: X-coordinate of the second point.
    :param y_2: Y-coordinate of the second point.
    :return: A tuple with the reordered points (X1, Y1, X2, Y2).
    """
    distance_1 = math.sqrt(x_1 ** 2 + y_1 ** 2)
    distance_2 = math.sqrt(x_2 ** 2 + y_2 ** 2)

    return (x_1, y_1, x_2, y_2) if distance_1 <= distance_2 else (x_2, y_2, x_1, y_1)


def line_length(x_1: float, y_1: float, x_2: float, y_2: float) -> float:
    """
    Computes the Euclidean distance between two points.

    :param x_1: X-coordinate of the first point.
    :param y_1: Y-coordinate of the first point.
    :param x_2: X-coordinate of the second point.
    :param y_2: Y-coordinate of the second point.
    :return: The length of the line segment.
    """
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)


def longest_line(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> str:
    """
    Determines which of the two lines is longer and formats it correctly,
    starting from the closer point to the origin.

    :param x1: X-coordinate of the first point of line 1.
    :param y1: Y-coordinate of the first point of line 1.
    :param x2: X-coordinate of the second point of line 1.
    :param y2: Y-coordinate of the second point of line 1.
    :param x3: X-coordinate of the first point of line 2.
    :param y3: Y-coordinate of the first point of line 2.
    :param x4: X-coordinate of the second point of line 2.
    :param y4: Y-coordinate of the second point of line 2.
    :return: The longest line formatted as "(X1, Y1)(X2, Y2)".
    """
    length_1 = line_length(x1, y1, x2, y2)
    length_2 = line_length(x3, y3, x4, y4)

    if length_1 >= length_2:
        x1, y1, x2, y2 = closest_point(x1, y1, x2, y2)
    else:
        x1, y1, x2, y2 = closest_point(x3, y3, x4, y4)

    return f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})'


if __name__ == '__main__':
    x1_input = float(input())
    y1_input = float(input())
    x2_input = float(input())
    y2_input = float(input())
    x3_input = float(input())
    y3_input = float(input())
    x4_input = float(input())
    y4_input = float(input())

    result = longest_line(
        x1=x1_input, y1=y1_input, x2=x2_input, y2=y2_input,
        x3=x3_input, y3=y3_input, x4=x4_input, y4=y4_input
    )
    print(result)
