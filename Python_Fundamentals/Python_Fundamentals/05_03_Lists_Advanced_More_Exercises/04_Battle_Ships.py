def count_destroyed_ships():
    n = int(input())

    field = [list(map(int, input().split())) for _ in range(n)]

    attacks = input().split()

    destroyed_ships = 0
    for attack in attacks:
        r, c = map(int, attack.split('-'))
        if field[r][c] > 0:
            field[r][c] -= 1
            if field[r][c] == 0:
                destroyed_ships += 1

    print(destroyed_ships)


if __name__ == '__main__':
    count_destroyed_ships()
