def calculate_parking_fee(days, hours_per_day):
    total_sum = 0

    for day in range(1, days + 1):
        daily_sum = 0
        for hour in range(1, hours_per_day + 1):
            if day % 2 == 0 and hour % 2 != 0:
                daily_sum += 2.50
            elif day % 2 != 0 and hour % 2 == 0:
                daily_sum += 1.25
            else:
                daily_sum += 1.00
        total_sum += daily_sum
        print(f'Day: {day} - {daily_sum:.2f} leva')

    print(f'Total: {total_sum:.2f} leva')


if __name__ == '__main__':
    days_count = int(input())
    hours_count = int(input())
    calculate_parking_fee(days=days_count, hours_per_day=hours_count)
