from typing import List


def faro_shuffle(deck: List[str], shuffles: int) -> List[str]:
    """
    Performs the specified number of faro shuffles on the given deck of cards.
    """

    for _ in range(shuffles):
        half = len(deck) // 2
        first_half = deck[:half]
        second_half = deck[half:]
        deck = [card for pair in zip(first_half, second_half) for card in pair]
    return deck


if __name__ == '__main__':
    deck_input = input().split()
    shuffle_count_input = int(input())
    result = faro_shuffle(deck=deck_input, shuffles=shuffle_count_input)
    print(result)
