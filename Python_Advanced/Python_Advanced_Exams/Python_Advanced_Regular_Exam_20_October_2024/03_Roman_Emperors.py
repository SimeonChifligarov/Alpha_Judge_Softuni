def list_roman_emperors(*args, **kwargs):
    status = {name: bool(s) for name, s in args}
    years = {name: int(y) for name, y in kwargs.items() if name in status}
    succ = [(n, years[n]) for n, ok in status.items() if ok and n in years]
    fail = [(n, years[n]) for n, ok in status.items() if not ok and n in years]
    succ.sort(key=lambda x: (-x[1], x[0]))
    fail.sort(key=lambda x: (x[1], x[0]))
    lines = [f"Total number of emperors: {len(years)}"]
    if succ:
        lines.append("Successful emperors:")
        lines += [f"****{n}: {y}" for n, y in succ]
    if fail:
        lines.append("Unsuccessful emperors:")
        lines += [f"****{n}: {y}" for n, y in fail]

    return "\n".join(lines)
