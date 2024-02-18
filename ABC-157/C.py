N, M = map(int, input().split())
s = []
c = []
for i in range(M):
    S, C = map(int, input().split())
    s.append(S)
    c.append(C)


for i in range(10 ** (N + 1)):
    Str = str(i)

    if len(Str) == N and all([Str[s[j] - 1] == str(c[j]) for j in range(M)]):
        print(Str)
        exit()

print(-1)
