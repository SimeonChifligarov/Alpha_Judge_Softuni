def process_exam_submissions() -> tuple[dict[str, int], dict[str, int]]:
    """
    Reads exam submissions and bans from input.
    Returns two dictionaries:
    - One storing usernames and their highest scores.
    - One storing programming languages and their total number of submissions.
    """
    user_scores = {}
    language_submissions = {}

    while True:
        data = input()
        if data == 'exam finished':
            break

        parts = data.split('-')

        if parts[1] == 'banned':
            username = parts[0]
            if username in user_scores:
                del user_scores[username]
        else:
            username, language, points = parts[0], parts[1], int(parts[2])

            if username not in user_scores or user_scores[username] < points:
                user_scores[username] = points

            if language not in language_submissions:
                language_submissions[language] = 0
            language_submissions[language] += 1

    return user_scores, language_submissions


def print_exam_results(user_scores: dict[str, int], language_submissions: dict[str, int]) -> None:
    """
    Prints the exam results and language submissions statistics.
    """
    print('Results:')
    for user, points in user_scores.items():
        print(f'{user} | {points}')

    print('Submissions:')
    for language, count in language_submissions.items():
        print(f'{language} - {count}')


if __name__ == '__main__':
    user_results, language_stats = process_exam_submissions()
    print_exam_results(user_scores=user_results, language_submissions=language_stats)
