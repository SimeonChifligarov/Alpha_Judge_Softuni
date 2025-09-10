def team_lineup(*args):
    countries = {}
    for player, country in args:
        countries.setdefault(country, []).append(player)
    sorted_countries = sorted(
        countries.items(),
        key=lambda x: (-len(x[1]), x[0])
    )
    result = []
    for country, players in sorted_countries:
        result.append(f"{country}:")
        for p in players:
            result.append(f"  -{p}")

    return "\n".join(result)
