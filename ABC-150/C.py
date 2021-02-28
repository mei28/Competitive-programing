import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

per = list(itertools.permutations(range(1, N + 1)))
p = per.index(P)
q = per.index(Q)
print(abs(p - q))
