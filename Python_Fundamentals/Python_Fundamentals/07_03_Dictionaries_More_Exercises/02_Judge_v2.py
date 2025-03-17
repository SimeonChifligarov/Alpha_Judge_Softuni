def process_contest_results():
    contest_data = {}
    user_total_points = {}

    while True:
        command = input()
        if command == 'no more time':
            break

        username, contest, points = command.split(' -> ', maxsplit=2)
        points = int(points)

        if contest not in contest_data:
            contest_data[contest] = {}

        if username in contest_data[contest]:
            if contest_data[contest][username] < points:
                user_total_points[username] += points - contest_data[contest][username]
                contest_data[contest][username] = points
        else:
            contest_data[contest][username] = points
            user_total_points[username] = user_total_points.get(username, 0) + points

    for contest, users in contest_data.items():
        print(f'{contest}: {len(users)} participants')
        sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
        for idx, (user, points) in enumerate(sorted_users, start=1):
            print(f'{idx}. {user} <::> {points}')

    print('Individual standings:')
    sorted_users = sorted(user_total_points.items(), key=lambda x: (-x[1], x[0]))
    for idx, (user, total_points) in enumerate(sorted_users, start=1):
        print(f'{idx}. {user} -> {total_points}')


if __name__ == '__main__':
    process_contest_results()
