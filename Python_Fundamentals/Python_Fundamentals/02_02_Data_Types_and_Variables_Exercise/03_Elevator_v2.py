n = int(input())
p = int(input())

courses = 0
courses += (n // p)
if not n % p == 0:
    courses += 1
print(courses)
