n, a, b = map(int, input().split())
X = list(map(int, input().split()))

pre = None
cost = 0

for i in range(n - 1):
    cost += min((X[i + 1] - X[i]) * a, b)

print(cost)
