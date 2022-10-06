n = int(input())
A = [int(input()) for _ in range(n)]


S = set()
for a in A:
    if a not in S:
        S.add(a)
    else:
        S.remove(a)

print(len(S))
