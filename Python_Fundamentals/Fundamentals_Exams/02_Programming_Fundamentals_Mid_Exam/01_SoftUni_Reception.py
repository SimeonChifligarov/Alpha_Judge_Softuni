a = int(input())
b = int(input())
c = int(input())
students = int(input())

per_hour = a + b + c
hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students -= per_hour

print(f"Time needed: {hours}h.")
