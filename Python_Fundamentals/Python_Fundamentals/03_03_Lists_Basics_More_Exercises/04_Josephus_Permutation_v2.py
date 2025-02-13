from typing import List


def josephus_permutation(people_list: List[int], step: int) -> List[int]:
    """
    Returns the Josephus permutation based on the list of people and the step count.
    Each k-th person in the circle is executed, continuing until no one remains.
    """

    result = []
    index = 0
    while people_list:
        index = (index + step - 1) % len(people_list)
        result.append(people_list.pop(index))

    return result


if __name__ == '__main__':
    people = list(map(int, input().split()))
    k = int(input())
    permutation = josephus_permutation(people_list=people, step=k)
    # print(f'[{",".join(map(str, permutation))}]')
    print(f'[{",".join([str(el) for el in permutation])}]')
