def start_spring(**kwargs):
    spring_dict = {}
    for obj, typ in kwargs.items():
        spring_dict.setdefault(typ, []).append(obj)

    for t in spring_dict:
        spring_dict[t].sort()

    sorted_types = sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for t, objs in sorted_types:
        result.append(f"{t}:")
        for o in objs:
            result.append(f"-{o}")

    return "\n".join(result)
