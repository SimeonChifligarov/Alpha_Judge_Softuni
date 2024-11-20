record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
water_resistance_time = (distance // 15) * 12.5
total_time_with_resistance = total_time + water_resistance_time

if total_time_with_resistance < record:
    print(f'Yes, he succeeded! The new world record is {total_time_with_resistance:.2f} seconds.')
else:
    time_diff = total_time_with_resistance - record
    print(f'No, he failed! He was {time_diff:.2f} seconds slower.')
