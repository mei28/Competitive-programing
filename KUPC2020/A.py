N = int(input())

X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(1, N):
    diff_x = abs(X[i - 1] - X[i])
    diff_y = abs(Y[i - 1] - Y[i])

    ans += diff_x + diff_y

print(ans)
