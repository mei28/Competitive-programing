n = int(input())

A = [int(input()) for _ in range(n)]

key = list(set(A))
key.sort()

dct = {k: i for i, k in enumerate(key)}

for a in A:
    print(dct[a])
