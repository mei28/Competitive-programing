N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            dx1 = X[k] - X[i]
            dy1 = Y[k] - Y[i]

            dx2 = X[j] - X[i]
            dy2 = Y[j] - Y[i]
            if dx1 * dy2 == dx2 * dy1:
                print("Yes")
                exit()

print("No")
