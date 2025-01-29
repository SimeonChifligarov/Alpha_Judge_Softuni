# Calculate how many courses will be needed to elevate n persons by using an elevator
# with capacity of p persons. The input holds two lines: the number of people n and the capacity p of the elevator.

import math

n = int(input())
p = int(input())

courses = math.ceil(n / p)
print(courses)
