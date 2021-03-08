N = int(input())
A = [0] + list(map(int, input().split())) + [0]

diffs = []

for i in range(1, N + 2):
    diffs.append(A[i] - A[i - 1])

_all = 0
for i in diffs:
    _all += abs(i)

for i in range(1, len(diffs)):
    print
    print(_all - abs(diffs[i - 1]) - abs(diffs[i]) + abs(diffs[i - 1] + diffs[i]))
