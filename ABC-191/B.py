N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []

for a in A:
    if a == X:
        continue
    else:
        print(a, end=" ")
