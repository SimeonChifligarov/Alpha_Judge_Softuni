def add_songs(*songs):
    songs_dict = {}
    for title, lyrics in songs:
        if title not in songs_dict:
            songs_dict[title] = []
        songs_dict[title].extend(lyrics)
    result = []
    for title, lyrics in songs_dict.items():
        result.append(f"- {title}")
        if lyrics:
            result.extend(lyrics)

    return "\n".join(result)
