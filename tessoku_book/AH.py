N, X, Y = map(int, input().split())

grundy = [0] * (100000 + 1)

for i in range(X, 100000 + 1):
    available = []
    for j in [X, Y]:
        nxt = i - j
        if nxt < 0:
            continue
        available.append(grundy[nxt])
    while grundy[i] in available:
        grundy[i] += 1

A = list(map(int, input().split()))

g = 0

for a in A:
    g ^= grundy[a]

if g == 0:
    print("Second")
else:
    print("First")
