import math

N, M = map(int, input().split())
S = input()
T = input()

gcd = math.gcd(N, M)
res = N * M // gcd

for i in range(0, res):
    if i * (res // M) >= N or i * (res // N) >= M:
        break
    # print(i, res // M, S[res // M], res // N, T[res // N])
    if S[i * (res // M)] != T[i * (res // N)]:
        print(-1)
        exit()

print(res)
