def fill_water_tank(lines: int) -> int:
    capacity = 255
    current_volume = 0
    for _ in range(lines):
        liters = int(input())
        if current_volume + liters > capacity:
            print('Insufficient capacity!')
        else:
            current_volume += liters
    return current_volume


if __name__ == '__main__':
    n = int(input())
    result = fill_water_tank(lines=n)
    print(result)
