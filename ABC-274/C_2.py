n = int(input())
A = list(map(int, input().split()))
D = [0 for _ in range(2 * n + 20)]

for i, a in enumerate(A):
    D[2 * (i + 1)] = D[(a)] + 1
    D[2 * (i + 1) + 1] = D[(a)] + 1
for i in range(1, 2 * n + 2):
    print(D[i])
