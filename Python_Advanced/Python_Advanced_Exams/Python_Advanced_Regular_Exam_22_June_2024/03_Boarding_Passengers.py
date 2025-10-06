def boarding_passengers(capacity, *groups):
    boarded = {}
    total_requested = sum(g[0] for g in groups)
    for count, program in groups:
        if count <= capacity:
            boarded[program] = boarded.get(program, 0) + count
            capacity -= count
        if capacity == 0:
            break

    result = "Boarding details by benefit plan:\n"
    sorted_boarded = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))
    for program, count in sorted_boarded:
        result += f"## {program}: {count} guests\n"
    if sum(boarded.values()) == total_requested:
        result += "All passengers are successfully boarded!"
    elif capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result
