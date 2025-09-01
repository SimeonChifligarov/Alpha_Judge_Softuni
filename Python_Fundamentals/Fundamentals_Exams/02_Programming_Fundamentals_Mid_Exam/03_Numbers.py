nums = list(map(int, input().split()))

avg = sum(nums) / len(nums)
greater = [x for x in nums if x > avg]

if not greater:
    print("No")
else:
    greater.sort(reverse=True)
    print(" ".join(map(str, greater[:5])))
