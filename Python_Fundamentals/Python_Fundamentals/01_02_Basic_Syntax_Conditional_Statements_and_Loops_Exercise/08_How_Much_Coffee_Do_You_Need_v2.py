def calculate_coffee_needed(events_list):
    coffee_count = 0
    for event in events_list:
        if event.lower() in ['coding', 'dog', 'cat', 'movie']:
            coffee_count += 2 if event.isupper() else 1
        if coffee_count > 5:
            return 'You need extra sleep'
    return coffee_count


if __name__ == '__main__':
    events_input = []
    while True:
        current_event = input()
        if current_event == 'END':
            break
        events_input.append(current_event)
    coffee_needed = calculate_coffee_needed(events_list=events_input)
    print(coffee_needed)
