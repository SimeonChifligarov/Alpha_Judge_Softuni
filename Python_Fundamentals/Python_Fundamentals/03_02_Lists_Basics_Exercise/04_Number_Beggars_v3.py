from typing import List


def beggars_collections(offers: List[int], beggars_count: int) -> List[int]:
    """
    Distributes the offers among beggars in a cyclic manner and returns the total collected by each beggar.
    """

    result = [0] * beggars_count
    for index, value in enumerate(offers):
        result[index % beggars_count] += value

    return result


if __name__ == '__main__':
    offers_input = list(map(int, input().split(', ')))
    beggars_count_input = int(input())
    res = beggars_collections(offers=offers_input, beggars_count=beggars_count_input)
    print(res)
