def calculate_actor_salaries(budget):
    while True:
        command = input()
        if command == 'ACTION':
            print(f'We are left with {budget:.2f} leva.')
            break

        actor_name = command
        if len(actor_name) > 15:
            salary = budget * 0.2
        else:
            salary = float(input())

        if salary > budget:
            needed = salary - budget
            print(f'We need {needed:.2f} leva for our actors.')
            break

        budget -= salary


budget_for_actors = float(input())
calculate_actor_salaries(budget_for_actors)
