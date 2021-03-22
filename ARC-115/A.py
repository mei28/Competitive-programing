N, M = map(int, input().split())
S = [input() for _ in range(N)]
odd = 0
even = 0

for i in range(N):
    if S[i].count("1") % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd * even)
