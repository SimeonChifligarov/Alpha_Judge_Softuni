def draw_cards(*args, **kwargs):
    monsters = []
    spells = []
    for name, ctype in args:
        if ctype == "monster":
            monsters.append(name)
        else:
            spells.append(name)
    for name, ctype in kwargs.items():
        if ctype == "monster":
            monsters.append(name)
        else:
            spells.append(name)
    monsters.sort(reverse=True)
    spells.sort()
    result = []
    if monsters:
        result.append("Monster cards:")
        for m in monsters:
            result.append(f"  ***{m}")
    if spells:
        result.append("Spell cards:")
        for s in spells:
            result.append(f"  $$${s}")

    return "\n".join(result)
