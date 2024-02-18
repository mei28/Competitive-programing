n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = [(a, b) for a, b in zip(A, B)]
CD = [(c, d) for c, d in zip(C, D)]

AB = list(sorted(AB, key=lambda x: x[0]))[::-1]
CD = list(sorted(CD, key=lambda x: x[0]))[::-1]

print(AB)
print(CD)
