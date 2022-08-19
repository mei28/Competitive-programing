n, k = map(int, input().split())
P = []
for i in range(n):
    P.append([sum(list(map(int, input().split()))), i])

P = list(sorted(P, key=lambda x: x[0], reverse=True))
threshold = P[k - 1][0]
P = list(sorted(P, key=lambda x: x[1]))
for p in P:
    p = p[0]
    if p + 300 >= threshold:
        print("Yes")
    else:
        print("No")
