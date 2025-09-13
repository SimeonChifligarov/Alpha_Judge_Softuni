from collections import Counter


def numbers_searching(*args):
    counts = Counter(args)
    duplicates = sorted([x for x, c in counts.items() if c > 1])
    mn, mx = min(args), max(args)
    missing = [x for x in range(mn, mx + 1) if x not in counts]

    return [missing[-1], duplicates]
