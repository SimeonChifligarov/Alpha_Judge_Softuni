# •	Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
# След това се четат многократно по един или два реда до команда 'ACTION' или до изчерпване на бюджета:
# •	Име на актьор - текст
# Ако името на актьора съдържа по-малко или равно на 15 брой символи:
# o	Възнаграждение - реално число в интервала [250.0… 1 000 000.0]

total_budget = float(input())

budget_left = total_budget
command = input()
while command != 'ACTION':
    actor = command
    if len(actor) > 15:
        actor_salary = budget_left * 0.20
    else:
        actor_salary = float(input())
    budget_left -= actor_salary
    if budget_left < 0:
        break

    command = input()

if budget_left < 0:
    print(f'We need {-budget_left :.2f} leva for our actors.')
else:
    print(f'We are left with {budget_left:.2f} leva.')
