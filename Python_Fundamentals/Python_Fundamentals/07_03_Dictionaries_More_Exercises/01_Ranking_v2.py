def process_contests() -> dict[str, str]:
    contests = {}
    while True:
        data = input()
        if data == 'end of contests':
            break
        contest, password = data.split(':', maxsplit=1)
        contests[contest] = password
    return contests


def process_submissions(contests: dict[str, str]) -> dict[str, dict[str, int]]:
    users = {}
    while True:
        data = input()
        if data == 'end of submissions':
            break
        contest, password, username, points = data.split('=>', maxsplit=3)
        points = int(points)

        if contest in contests and contests[contest] == password:
            if username not in users:
                users[username] = {}
            if contest not in users[username] or users[username][contest] < points:
                users[username][contest] = points
    return users


def get_best_candidate(users: dict[str, dict[str, int]]) -> tuple[str, int]:
    return max(((user, sum(contests.values())) for user, contests in users.items()), key=lambda x: x[1])


def print_results(users: dict[str, dict[str, int]]) -> None:
    best_user, best_points = get_best_candidate(users)
    print(f'Best candidate is {best_user} with total {best_points} points.')

    print('Ranking:')
    for user in sorted(users):
        print(user)
        for contest, points in sorted(users[user].items(), key=lambda x: -x[1]):
            print(f'#  {contest} -> {points}')


if __name__ == '__main__':
    contests_data = process_contests()
    users_data = process_submissions(contests=contests_data)
    print_results(users=users_data)
