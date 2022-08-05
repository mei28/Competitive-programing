n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = [0] * (n)

min_time = min(T)
min_index = T.index(min_time)

now_t = T[min_index]
ans = [0] * n

for i in range(n):
    now_i = (min_index + i) % n
    now_t = min(now_t, T[now_i])
    ans[now_i] = now_t
    now_t += S[now_i]

for a in ans:
    print(a)
