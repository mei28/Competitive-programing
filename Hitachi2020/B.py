A, B, M = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Q = [list(map(int, input().split())) for i in range(M)]

ans = [min(As) + min(Bs)]

for q in Q:
    x, y, c = q[0], q[1], q[2]
    ans.append(As[x - 1] + Bs[y - 1] - c)
print(min(ans))
