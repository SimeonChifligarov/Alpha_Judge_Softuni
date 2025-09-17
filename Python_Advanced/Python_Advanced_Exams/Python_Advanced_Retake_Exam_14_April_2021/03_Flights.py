def flights(*args):
    result = {}
    i = 0
    while i < len(args):
        if args[i] == "Finish":
            break
        destination = args[i]
        passengers = args[i + 1]
        if destination not in result:
            result[destination] = 0
        result[destination] += passengers
        i += 2

    return result
