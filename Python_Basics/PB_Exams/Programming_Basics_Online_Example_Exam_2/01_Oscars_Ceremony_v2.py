def calculate_event_cost(venue_rent):
    statue_cost = venue_rent * 0.7
    catering_cost = statue_cost * 0.85
    sound_cost = catering_cost / 2
    total_cost = venue_rent + statue_cost + catering_cost + sound_cost
    return f'{total_cost:.2f}'


current_venue_rent = int(input())
print(calculate_event_cost(venue_rent=current_venue_rent))
