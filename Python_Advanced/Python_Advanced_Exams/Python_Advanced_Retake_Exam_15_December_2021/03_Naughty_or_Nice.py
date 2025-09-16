def naughty_or_nice_list(kids, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    for command in args:
        number, status = command.split("-")
        number = int(number)
        matches = [kid for kid in kids if kid[0] == number]
        if len(matches) == 1:
            _, name = matches[0]
            if status == "Nice":
                nice.append(name)
            else:
                naughty.append(name)
            kids.remove(matches[0])

    for name, status in kwargs.items():
        matches = [kid for kid in kids if kid[1] == name]
        if len(matches) == 1:
            num, _ = matches[0]
            if status == "Nice":
                nice.append(name)
            else:
                naughty.append(name)
            kids.remove(matches[0])

    for _, name in kids:
        not_found.append(name)

    result = []
    if nice:
        result.append(f"Nice: {', '.join(nice)}")
    if naughty:
        result.append(f"Naughty: {', '.join(naughty)}")
    if not_found:
        result.append(f"Not found: {', '.join(not_found)}")

    return "\n".join(result)
