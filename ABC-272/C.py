n = int(input())
A = list(map(int, input().split()))
A.sort()
even = [a for a in A if a % 2 == 0]
odds = [a for a in A if a % 2 == 1]


ans = -1

if len(even) >= 2:
    ans = max(ans, even[-1] + even[-2])
if len(odds) >= 2:
    ans = max(ans, odds[-1] + odds[-2])

print(ans)
