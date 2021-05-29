N, Q = map(int, input().split())
S = input()

AC = [0] * (N + 10)

for i in range(N - 1):
    AC[i + 1] += AC[i] + (1 if S[i] == "A" and S[i + 1] == "C" else 0)

for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(AC[r] - AC[l])
