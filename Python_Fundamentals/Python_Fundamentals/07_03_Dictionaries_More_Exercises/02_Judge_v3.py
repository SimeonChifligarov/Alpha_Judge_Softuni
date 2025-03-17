def process_input() -> tuple[dict[str, dict[str, int]], dict[str, int], list[str]]:
    contests = {}
    user_total_points = {}
    contest_order = []

    while True:
        data = input()
        if data == 'no more time':
            break
        username, contest, points = data.split(' -> ', maxsplit=2)
        points = int(points)

        if contest not in contests:
            contests[contest] = {}
            contest_order.append(contest)

        if username not in contests[contest] or contests[contest][username] < points:
            if username in contests[contest]:
                user_total_points[username] -= contests[contest][username]
            contests[contest][username] = points
            user_total_points[username] = user_total_points.get(username, 0) + points

    return contests, user_total_points, contest_order


def print_results(contests: dict[str, dict[str, int]], user_total_points: dict[str, int],
                  contest_order: list[str]) -> None:
    for contest in contest_order:
        participants = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))
        print(f'{contest}: {len(participants)} participants')
        for index, (username, points) in enumerate(participants, start=1):
            print(f'{index}. {username} <::> {points}')

    print('Individual standings:')
    individual_rankings = sorted(user_total_points.items(), key=lambda x: (-x[1], x[0]))
    for index, (username, total_points) in enumerate(individual_rankings, start=1):
        print(f'{index}. {username} -> {total_points}')


if __name__ == '__main__':
    contests_data, user_points_data, contest_order_list = process_input()
    print_results(contests=contests_data, user_total_points=user_points_data, contest_order=contest_order_list)
