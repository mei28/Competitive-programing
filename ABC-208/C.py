n, k = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i, a in enumerate(A):
    B.append([a, i, 0])

tmp = k // n
k %= n
B = list(sorted(B, key=lambda x: x[0]))

for i in range(k):
    B[i][2] += 1

B = list(sorted(B, key=lambda x: x[1]))

for i in B:
    print(i[2] + tmp)
