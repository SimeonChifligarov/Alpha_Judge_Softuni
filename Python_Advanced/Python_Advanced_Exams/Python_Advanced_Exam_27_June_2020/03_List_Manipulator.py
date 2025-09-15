def list_manipulator(numbers, command, position, *args):
    if command == "add":
        if position == "beginning":
            numbers = list(args) + numbers
        else:
            numbers.extend(args)
    else:
        count = args[0] if args else 1
        if position == "beginning":
            numbers = numbers[count:]
        else:
            numbers = numbers[:-count] if count <= len(numbers) else []

    return numbers
