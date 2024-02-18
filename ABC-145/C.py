import math

n = int(input())

X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


l = 0
for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        l += math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)

print(l * 2 / n)
