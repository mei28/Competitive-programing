N, K = map(int, input().split())
points = []
for i in range(N):
    a, b = map(int, input().split())
    points.append(b)
    points.append(a - b)

points.sort(reverse=True)

ans = sum(points[:K])

print(ans)
