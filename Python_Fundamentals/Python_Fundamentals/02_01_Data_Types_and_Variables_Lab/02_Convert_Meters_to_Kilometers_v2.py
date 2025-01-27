def convert_meters_to_kilometers(distance_in_meters):
    return distance_in_meters / 1000


if __name__ == '__main__':
    meters = int(input())
    kilometers = convert_meters_to_kilometers(distance_in_meters=meters)
    print(f'{kilometers:.2f}')
