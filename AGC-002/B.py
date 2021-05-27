N, M = map(int, input().split())
nums = [1] * N
can = [False] * N
can[0] = True

for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    if can[a]:
        can[b] = True
    if nums[a] == 1:
        can[a] = False
    nums[a] -= 1
    nums[b] += 1

ans = 0

for i in range(N):
    if can[i] and nums[i]:
        ans += 1

print(ans)
