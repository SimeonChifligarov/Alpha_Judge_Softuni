from math import ceil


def calculate_courses(people: int, capacity: int) -> int:
    return ceil(people / capacity)


if __name__ == '__main__':
    total_people = int(input())
    elevator_capacity = int(input())
    result = calculate_courses(people=total_people, capacity=elevator_capacity)
    print(result)
