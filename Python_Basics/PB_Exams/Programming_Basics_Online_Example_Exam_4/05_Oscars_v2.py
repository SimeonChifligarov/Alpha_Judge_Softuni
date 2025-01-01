def calculate_actor_points(actor_name, academy_points, judges_count):
    total_points = academy_points

    for _ in range(judges_count):
        judge_name = input()
        judge_points = float(input())
        points_earned = (len(judge_name) * judge_points) / 2
        total_points += points_earned

        if total_points > 1250.5:
            print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
            return

    needed_points = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {needed_points:.1f} more!')


actor = input()
initial_points = float(input())
judges = int(input())

calculate_actor_points(actor, initial_points, judges)
