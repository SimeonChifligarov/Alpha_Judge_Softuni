def movie_organizer(*movies):
    genres = {}
    for name, genre in movies:
        genres.setdefault(genre, []).append(name)
    for g in genres:
        genres[g].sort()
    sorted_genres = sorted(genres.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for genre, names in sorted_genres:
        result.append(f"{genre} - {len(names)}")
        for name in names:
            result.append(f"* {name}")

    return "\n".join(result)
