# using while True

goal = 10000
total_steps = 0

while True:
    command = input()
    if command == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        if total_steps >= goal:
            print('Goal reached! Good job!')
            print(f'{total_steps - goal} steps over the goal!')
        else:
            print(f'{goal - total_steps} more steps to reach goal.')
        break
    else:
        steps = int(command)
        total_steps += steps
        if total_steps >= goal:
            print('Goal reached! Good job!')
            print(f'{total_steps - goal} steps over the goal!')
            break
