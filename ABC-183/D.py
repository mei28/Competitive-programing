# N, W = map(int, input().split())
# S, T, P = [], [], []

# for i in range(N):
#     s, t, p = map(int, input().split())
#     S.append(s)
#     T.append(t)
#     P.append(p)

# print(S)
# print(T)
# print(P)

n, w = map(int, input().split())

demand = [0] * 22000000
for _ in range(n):
    s, t, p = map(int, input().split())
    demand[s] += p
    demand[t] -= p

for i in range(1, 2200000):
    demand[i] += demand[i-1]

if max(demand) <= w:
    print('Yes')
else:
    print('No')