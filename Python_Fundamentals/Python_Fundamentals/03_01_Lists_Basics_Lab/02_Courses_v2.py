from typing import List


def collect_courses(count: int) -> List[str]:
    courses = [input() for _ in range(count)]
    return courses


if __name__ == '__main__':
    count_input = int(input())
    result = collect_courses(count=count_input)
    print(result)
