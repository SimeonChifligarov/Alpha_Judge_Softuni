jobs = list(map(int, input().split(", ")))
target_index = int(input())

indexed_jobs = [(j, i) for i, j in enumerate(jobs)]
indexed_jobs.sort(key=lambda x: (x[0], jobs.index(x[0])))

time = 0
for job, idx in indexed_jobs:
    time += job
    if idx == target_index:
        print(time)
        break
