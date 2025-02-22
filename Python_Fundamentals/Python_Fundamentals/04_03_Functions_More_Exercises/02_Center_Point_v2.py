import math


def calculate_distance_squared(x: float, y: float) -> float:
    return x ** 2 + y ** 2


def closest_point_to_origin(x1: float, y1: float, x2: float, y2: float) -> tuple[int, int]:
    if calculate_distance_squared(x1, y1) <= calculate_distance_squared(x2, y2):
        return math.floor(x1), math.floor(y1)
    return math.floor(x2), math.floor(y2)


def main() -> None:
    x1, y1 = float(input()), float(input())
    x2, y2 = float(input()), float(input())

    closest_point = closest_point_to_origin(x1, y1, x2, y2)
    print(closest_point)


if __name__ == "__main__":
    main()
