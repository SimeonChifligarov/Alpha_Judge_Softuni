def climbing_record(current_record, distance, time_per_meter):
    total_time = distance * time_per_meter
    delay = (distance // 50) * 30
    total_time += delay

    if total_time < current_record:
        print(f'Yes! The new record is {total_time:.2f} seconds.')
    else:
        print(f'No! He was {(total_time - current_record):.2f} seconds slower.')


if __name__ == '__main__':
    record_in_seconds = float(input())
    climbing_distance = float(input())
    time_per_meter_input = float(input())
    climbing_record(current_record=record_in_seconds, distance=climbing_distance, time_per_meter=time_per_meter_input)
