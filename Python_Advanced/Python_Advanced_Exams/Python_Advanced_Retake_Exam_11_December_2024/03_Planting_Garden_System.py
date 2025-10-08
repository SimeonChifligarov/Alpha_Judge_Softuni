def plant_garden(available_space, *allowed, **requests):
    allowed_map = {t: float(s) for t, s in allowed}
    remaining = {k: int(v) for k, v in requests.items() if k in allowed_map}
    planted = {}
    for plant in sorted(requests):
        if plant not in allowed_map:
            continue
        per = allowed_map[plant]
        need = remaining.get(plant, 0)
        if need <= 0:
            continue
        can = int((available_space + 1e-9) // per)
        to_plant = min(need, can)
        if to_plant > 0:
            planted[plant] = planted.get(plant, 0) + to_plant
            available_space -= per * to_plant
            remaining[plant] -= to_plant
        if available_space <= 0:
            break

    all_fulfilled = all(v == 0 for v in remaining.values())
    msg = f"All plants were planted! Available garden space: {max(0.0, available_space):.1f} sq meters." if all_fulfilled else "Not enough space to plant all requested plants!"
    lines = ["Planted plants:"] + [f"{k}: {planted[k]}" for k in sorted(planted)]
    return "\n".join([msg] + lines)
