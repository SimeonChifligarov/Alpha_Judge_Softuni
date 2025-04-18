from collections import deque


def collect_colors(pieces: list[str]) -> None:
    """
    This function makes colors by matching and modifying string pieces.

    Args:
        pieces (list[str]): List with pieces of strings.

    Returns:
        None
    """
    parts = deque(pieces)
    found_colors = []
    primary = {'red', 'yellow', 'blue'}
    secondary = {
        'orange': {'red', 'yellow'},
        'purple': {'red', 'blue'},
        'green': {'yellow', 'blue'},
    }
    while parts:
        left = parts.popleft()
        right = parts.pop() if parts else ''
        attempt = left + right
        if attempt in primary or attempt in secondary:
            found_colors.append(attempt)
            continue
        attempt = right + left
        if attempt in primary or attempt in secondary:
            found_colors.append(attempt)
            continue
        new_left = left[:-1]
        new_right = right[:-1]
        mid = len(parts) // 2
        if new_left:
            parts.insert(mid, new_left)
        if new_right:
            parts.insert(mid, new_right)
    final = []
    for color in found_colors:
        if color in primary:
            final.append(color)
        else:
            needed = secondary[color]
            if needed.issubset(set(found_colors)):
                final.append(color)
    print(final)


if __name__ == '__main__':
    input_parts = input().split()
    collect_colors(pieces=input_parts)
