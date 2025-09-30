def forecast(*locations):
    order = {"Sunny": 1, "Cloudy": 2, "Rainy": 3}
    sorted_locations = sorted(locations, key=lambda x: (order[x[1]], x[0]))

    return "\n".join(f"{place} - {weather}" for place, weather in sorted_locations)
