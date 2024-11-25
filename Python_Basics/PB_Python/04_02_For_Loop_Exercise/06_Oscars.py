TOTAL_POINTS_THRESHOLD = 1250.5

actor_name = input()
academy_points = float(input())
n = int(input())

total_points = academy_points

for _ in range(n):
    evaluator_name = input()
    evaluator_points = float(input())

    total_points += (len(evaluator_name) * evaluator_points) / 2

    if total_points > TOTAL_POINTS_THRESHOLD:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    needed_points = TOTAL_POINTS_THRESHOLD - total_points
    print(f'Sorry, {actor_name} you need {needed_points:.1f} more!')
