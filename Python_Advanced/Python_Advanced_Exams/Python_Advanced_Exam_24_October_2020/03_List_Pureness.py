from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    best_pureness = float("-inf")
    best_rotation = 0
    for rotation in range(k + 1):
        pureness = sum(idx * val for idx, val in enumerate(numbers))
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        numbers.rotate(1)

    return f"Best pureness {best_pureness} after {best_rotation} rotations"
