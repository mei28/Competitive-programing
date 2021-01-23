N = int(input())
A = list(map(int, input().split())) + [0]

cand = []

for i in range(N):
    while len(cand) >= 1 and A[cand[-1]] > A[i]:
        ans = max(ans, (i-cand[-1])) * A[cand[-1]]
        cand.pop()
    cand.append()

print(ans)
