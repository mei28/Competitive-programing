import itertools

N, K = map(int, input().split())
T = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    T[i] = list(map(int, input().split()))

a = [i for i in range(1, N)]
p = itertools.permutations(a, N - 1)

cnt = 0
pre_i = 0

for c in p:
    pre_i = 0
    sum_ = 0
    for i in c:
        sum_ += T[pre_i][i]
        pre_i = i
    sum_ += T[pre_i][0]
    if sum_ == K:
        cnt += 1

print(cnt)
