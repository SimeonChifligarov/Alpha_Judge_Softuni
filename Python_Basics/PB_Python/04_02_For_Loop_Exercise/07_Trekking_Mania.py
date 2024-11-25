n = int(input())

musala = montblanc = kilimanjaro = k2 = everest = 0

for _ in range(n):
    group_size = int(input())

    if group_size <= 5:
        musala += group_size
    elif group_size <= 12:
        montblanc += group_size
    elif group_size <= 25:
        kilimanjaro += group_size
    elif group_size <= 40:
        k2 += group_size
    else:
        everest += group_size

total_climbers = musala + montblanc + kilimanjaro + k2 + everest

groups = [
    (c / total_climbers) * 100 for c in [
        musala,
        montblanc,
        kilimanjaro,
        k2,
        everest,
    ]
]

for gr in groups:
    print(f'{gr:.2f}%')
