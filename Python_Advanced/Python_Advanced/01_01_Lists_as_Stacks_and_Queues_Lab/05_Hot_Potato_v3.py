from collections import deque
from typing import List


def hot_potato_game(kids: List[str], toss_count: int) -> List[str]:
    """
    Simulates the Hot Potato game and returns the sequence of events,
    showing who gets removed each round and who is the last kid remaining.
    """
    sequence = []
    queue = deque(kids)
    while len(queue) > 1:
        for _ in range(toss_count - 1):
            queue.append(queue.popleft())
        removed = queue.popleft()
        sequence.append(f'Removed {removed}')
    last = queue.popleft()
    sequence.append(f'Last is {last}')
    return sequence


if __name__ == '__main__':
    kids_input = input().split()
    toss_input = int(input())
    result_output = hot_potato_game(kids=kids_input, toss_count=toss_input)
    for event in result_output:
        print(event)
