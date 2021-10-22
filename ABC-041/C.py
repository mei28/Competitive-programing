n = int(input())
A = list(map(int, input().split()))

B = []
for i, h in enumerate(A):
    i += 1
    B.append((h, i))

B = list(sorted(B, key=lambda x: x[0], reverse=True))

for i in B:
    print(i[1])
