import math
n = int(input())
A =[list(map(int,input().split())) for _ in range(n)]

ans = -1
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        xi,yi = A[i]
        xj,yj = A[j]
        ans = max(ans, (xi-xj)**2+(yi-yj)**2 )

print(math.sqrt(ans))
