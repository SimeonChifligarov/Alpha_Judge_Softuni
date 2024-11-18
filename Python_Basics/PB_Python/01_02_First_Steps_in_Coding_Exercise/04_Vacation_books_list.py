pages_in_book = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

total_hours_needed = pages_in_book // pages_per_hour  # by examples in problem definition
hours_per_day = total_hours_needed / days_for_reading

print(hours_per_day)
