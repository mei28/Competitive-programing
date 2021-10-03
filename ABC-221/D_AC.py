from typing import List, Tuple

N: int = 200010
ans: List[int] = [0] * N

n = int(input())
x: List[Tuple[int, int]] = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append((a, 1))
    x.append((a + b, -1))

x = list(sorted(x, key=lambda x: x[0]))

cnt: int = 0
for i in range(len(x) - 1):
    cnt += x[i][1]
    ans[cnt] += x[i + 1][0] - x[i][0]

for i in range(n - 1):
    print(ans[i + 1], end=" ")
print(ans[n])
