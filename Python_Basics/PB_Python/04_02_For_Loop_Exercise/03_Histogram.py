p1_count = p2_count = p3_count = p4_count = p5_count = 0

num_count = int(input())

for _ in range(num_count):
    current_number = int(input())

    if current_number < 200:
        p1_count += 1
    elif current_number < 400:
        p2_count += 1
    elif current_number < 600:
        p3_count += 1
    elif current_number < 800:
        p4_count += 1
    elif current_number >= 800:
        p5_count += 1

percents = [
    (p / num_count) * 100 for p in [
        p1_count,
        p2_count,
        p3_count,
        p4_count,
        p5_count,
    ]
]

for p in percents:
    print(f'{p:.2f}%')
