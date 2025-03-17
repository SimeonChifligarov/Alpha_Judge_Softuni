def process_final_ranking():
    contest_credentials = {}
    user_scores = {}

    while True:
        command = input()
        if command == 'end of contests':
            break
        contest, password = command.split(':', maxsplit=1)
        contest_credentials[contest] = password

    while True:
        command = input()
        if command == 'end of submissions':
            break

        contest, password, username, points = command.split('=>', maxsplit=3)
        points = int(points)

        if contest in contest_credentials and contest_credentials[contest] == password:
            if username not in user_scores:
                user_scores[username] = {}

            user_scores[username][contest] = max(user_scores[username].get(contest, 0), points)

    best_user = max(user_scores, key=lambda user: sum(user_scores[user].values()))
    best_total_points = sum(user_scores[best_user].values())

    print(f'Best candidate is {best_user} with total {best_total_points} points.')

    print('Ranking:')
    for username in sorted(user_scores):
        print(username)
        for contest, points in sorted(user_scores[username].items(), key=lambda x: -x[1]):
            print(f'#  {contest} -> {points}')


if __name__ == '__main__':
    process_final_ranking()
