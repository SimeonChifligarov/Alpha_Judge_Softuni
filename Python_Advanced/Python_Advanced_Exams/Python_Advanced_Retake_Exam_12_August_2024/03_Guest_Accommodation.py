def accommodate(*groups, **rooms_kwargs):
    rooms = [[int(v), int(k.split("_")[1])] for k, v in rooms_kwargs.items()]
    rooms.sort(key=lambda x: (x[0], x[1]))
    accommodations = []
    unaccommodated = 0
    for g in groups:
        exact = -1
        bigger = -1
        for i, (cap, num) in enumerate(rooms):
            if cap == g:
                exact = i
                break
            if cap > g and bigger == -1:
                bigger = i
        idx = exact if exact != -1 else bigger
        if idx == -1:
            unaccommodated += g
        else:
            cap, num = rooms.pop(idx)
            accommodations.append((num, g))
    lines = []
    if accommodations:
        lines.append(f"A total of {len(accommodations)} accommodations were completed!")
        for num, g in sorted(accommodations, key=lambda x: x[0]):
            lines.append(f"<Room {num} accommodates {g} guests>")
    else:
        lines.append("No accommodations were completed!")
    if unaccommodated > 0:
        lines.append(f"Guests with no accommodation: {unaccommodated}")
    if rooms:
        lines.append(f"Empty rooms: {len(rooms)}")
    return "\n".join(lines)
