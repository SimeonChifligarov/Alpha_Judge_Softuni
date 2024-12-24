def track_training(target_height):
    current_height = target_height - 30
    total_jumps = 0

    while current_height <= target_height:
        failed_attempts = 0
        for _ in range(3):
            jump = int(input())
            total_jumps += 1
            if jump > current_height:
                current_height += 5
                break
            else:
                failed_attempts += 1
            if failed_attempts == 3:
                return f'Tihomir failed at {current_height}cm after {total_jumps} jumps.'

        if current_height > target_height:
            return f'Tihomir succeeded, he jumped over {current_height - 5}cm after {total_jumps} jumps.'


c_target_height = int(input())

# res = track_training(target_height=c_target_height)
# print(res)
print(track_training(target_height=c_target_height))
