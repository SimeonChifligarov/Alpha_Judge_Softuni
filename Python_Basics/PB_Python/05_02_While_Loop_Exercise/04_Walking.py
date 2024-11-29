# using while-else

goal = 10000
total_steps = 0
command = input()

while command != 'Going home':
    steps = int(command)
    total_steps += steps
    if total_steps >= goal:
        print('Goal reached! Good job!')
        print(f'{total_steps - goal} steps over the goal!')
        break
    command = input()
else:
    steps_home = int(input())
    total_steps += steps_home
    if total_steps >= goal:
        print('Goal reached! Good job!')
        print(f'{total_steps - goal} steps over the goal!')
    else:
        print(f'{goal - total_steps} more steps to reach goal.')
