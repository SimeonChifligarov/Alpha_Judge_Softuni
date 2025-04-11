from collections import deque


def crossroads_simulation(green_duration: int, free_window_duration: int) -> None:
    """
    This function keeps track of cars at a crossroads.
    It checks if cars pass safely or if a crash happens.

    Args:
        green_duration: Seconds for green light.
        free_window_duration: Seconds for free window after green light.

    Returns:
        None
    """
    cars_queue = deque()
    passed_cars = 0

    while True:
        line_input = input()
        if line_input == 'END':
            print('Everyone is safe.')
            print(f'{passed_cars} total cars passed the crossroads.')
            break
        if line_input == 'green':
            current_green = green_duration
            current_free = free_window_duration
            while cars_queue and current_green > 0:
                current_car = cars_queue.popleft()
                if len(current_car) <= current_green:
                    current_green -= len(current_car)
                    passed_cars += 1
                else:
                    remaining_length = len(current_car) - current_green
                    if remaining_length <= current_free:
                        passed_cars += 1
                        current_green = 0
                    else:
                        hit_index = current_green + current_free
                        print('A crash happened!')
                        print(f'{current_car} was hit at {current_car[hit_index]}.')
                        return
        else:
            cars_queue.append(line_input)


if __name__ == '__main__':
    green_input = int(input())
    free_input = int(input())
    crossroads_simulation(green_duration=green_input, free_window_duration=free_input)
