def manage_course_schedule(schedule: list[str], commands: list[str]) -> list[str]:
    """
    Modifies the course schedule based on given commands.
    Returns the final schedule list.
    """
    for com in commands:
        parts = com.split(':')
        action = parts[0]

        if action == 'Add':
            lesson = parts[1]
            if lesson not in schedule:
                schedule.append(lesson)

        elif action == 'Insert':
            lesson, index = parts[1], int(parts[2])
            if lesson not in schedule:
                schedule.insert(index, lesson)

        elif action == 'Remove':
            lesson = parts[1]
            if lesson in schedule:
                schedule.remove(lesson)
                exercise = f'{lesson}-Exercise'
                if exercise in schedule:
                    schedule.remove(exercise)

        elif action == 'Swap':
            lesson_1, lesson_2 = parts[1], parts[2]
            if lesson_1 in schedule and lesson_2 in schedule:
                index_1, index_2 = schedule.index(lesson_1), schedule.index(lesson_2)
                schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

                exercise_1, exercise_2 = f'{lesson_1}-Exercise', f'{lesson_2}-Exercise'
                if exercise_1 in schedule:
                    schedule.remove(exercise_1)
                    schedule.insert(index_2 + 1, exercise_1)
                if exercise_2 in schedule:
                    schedule.remove(exercise_2)
                    schedule.insert(index_1 + 1, exercise_2)

        elif action == 'Exercise':
            lesson = parts[1]
            exercise = f'{lesson}-Exercise'
            if lesson in schedule and exercise not in schedule:
                lesson_index = schedule.index(lesson)
                schedule.insert(lesson_index + 1, exercise)
            elif lesson not in schedule:
                schedule.append(lesson)
                schedule.append(exercise)

    return [f'{i + 1}.{schedule[i]}' for i in range(len(schedule))]


if __name__ == '__main__':
    schedule_input = input().split(', ')
    commands_input = []

    while True:
        command = input()
        if command == 'course start':
            break
        commands_input.append(command)

    result = manage_course_schedule(schedule=schedule_input, commands=commands_input)
    print('\n'.join(result))
