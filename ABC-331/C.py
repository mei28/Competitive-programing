from bisect import bisect_right
from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))


sorted_A = sorted(A)
cumulative_sum = list(accumulate(sorted_A))

results = []
for a in A:
    idx = bisect_right(sorted_A, a)

    sum_greater = cumulative_sum[-1] - cumulative_sum[idx - 1] if idx < len(A) else 0
    results.append(sum_greater)

print(*results)
