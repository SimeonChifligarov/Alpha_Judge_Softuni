def list_manipulator(numbers, command, position, *args):
    if command == "add":
        if position == "beginning":
            numbers[:] = list(args) + numbers
        else:
            numbers.extend(args)
    else:
        count = args[0] if args else 1
        if position == "beginning":
            del numbers[:count]
        else:
            if count <= len(numbers):
                del numbers[-count:]
            else:
                numbers.clear()
    return numbers
