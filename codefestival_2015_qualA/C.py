n, t = map(int, input().split())
s = 0
X = []
for i in range(n):
    a, b  = map(int, input().split())
    s +=a
    X.append(-a+b)
if s <= t:
    print(0)
    exit()
X.sort()
for i in range(n):
    x = X[i]
    s += x
    if s <= t:
        print(i+1)
        exit()
print(-1)
