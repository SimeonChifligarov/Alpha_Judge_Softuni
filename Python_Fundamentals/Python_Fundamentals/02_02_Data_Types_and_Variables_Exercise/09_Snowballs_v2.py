def find_highest_snowball_value(num_snowballs: int, snowball_data: list) -> str:
    max_value = 0
    best_snowball = ''
    for i in range(num_snowballs):
        weight = snowball_data[i * 3]
        time = snowball_data[i * 3 + 1]
        quality = snowball_data[i * 3 + 2]
        value = (weight / time) ** quality
        if value > max_value:
            max_value = value
            best_snowball = f'{weight} : {time} = {int(value)} ({quality})'
    return best_snowball


if __name__ == '__main__':
    number_of_snowballs = int(input())
    sb_data = [int(input()) for _ in range(number_of_snowballs * 3)]
    result = find_highest_snowball_value(num_snowballs=number_of_snowballs, snowball_data=sb_data)
    print(result)
