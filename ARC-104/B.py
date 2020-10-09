N, S = input().split()
N = int(N)

cnt = 0
for p in range(1, N):
    if 2 * p > N:
        break
    stride = 2 * p
    for i in range(0, N - stride + 1):
        s = S[i: i + stride]
        n_a = 0
        n_t = 0
        n_g = 0
        n_c = 0
        n_a = s.count('A')
        n_t = s.count('T')
        n_g = s.count('G')
        n_c = s.count('C')
        if (n_a == n_t and n_g == n_c):
            cnt += 1
        # print(s, n_a, n_t, n_g, n_c)
print(cnt)
