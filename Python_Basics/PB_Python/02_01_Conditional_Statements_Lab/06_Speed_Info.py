speed = float(input())

if speed <= 10:
    print('slow')
elif speed <= 50:  # speed (10; 50]
    print('average')
elif speed <= 150:  # speed (50; 150]
    print('fast')
elif speed <= 1_000:  # speed (150; 1_000]
    print('ultra fast')
else:  # speed (1_000; inf)
    print('extremely fast')
