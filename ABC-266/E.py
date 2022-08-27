import math

n = int(input())

ans = 3.5

for i in range(1, n):
    ans2 = 0
    for d in range(1, 7):
        ans2 += max(ans, d) / 6
    ans = ans2

print(ans)
