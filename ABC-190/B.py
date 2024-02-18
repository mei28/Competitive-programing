N, S, D = map(int, input().split())
X, Y = [], []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


for x, y in zip(X, Y):
    if x < S and y > D:
        print("Yes")
        exit()
print("No")
