def calculate_easter_trip_cost(destination, date_range, nights_count):
    price_chart = {
        "France": {"21-23": 30, "24-27": 35, "28-31": 40},
        "Italy": {"21-23": 28, "24-27": 32, "28-31": 39},
        "Germany": {"21-23": 32, "24-27": 37, "28-31": 43},
    }

    cost_per_night = price_chart[destination][date_range]
    total_cost = cost_per_night * nights_count
    return f"Easter trip to {destination} : {total_cost:.2f} leva."


destination_input = input()
date_range_input = input()
nights_input = int(input())

print(calculate_easter_trip_cost(destination_input, date_range_input, nights_input))
