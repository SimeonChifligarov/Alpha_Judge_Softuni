n = int(input())
numbers = [int(input()) for _ in range(n * 2)]

pairs_sums = [numbers[i] + numbers[i + 1] for i in range(0, n * 2, 2)]

if all(x == pairs_sums[0] for x in pairs_sums):
    print(f'Yes, value={pairs_sums[0]}')
else:
    max_diff = max(abs(pairs_sums[i] - pairs_sums[i + 1]) for i in range(len(pairs_sums) - 1))
    print(f'No, maxdiff={max_diff}')
