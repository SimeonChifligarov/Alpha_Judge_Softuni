def words_sorting(*words):
    values = {word: sum(ord(ch) for ch in word) for word in words}
    total = sum(values.values())
    if total % 2 == 1:
        sorted_items = sorted(values.items(), key=lambda x: -x[1])
    else:
        sorted_items = sorted(values.items(), key=lambda x: x[0])

    return "\n".join(f"{k} - {v}" for k, v in sorted_items)
