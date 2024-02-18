X, K, D = map(int, input().split())

now = X
visited = {}
left = K
prev = X
breaked = False

if X >= K * D:
    print(abs(abs(X) - abs(K * D)))
    exit()

for i in range(K):
    if now >= D:
        k = now // D
    else:
        k = 1
    left -= k
    prev = now
    next_p = now + k * D
    next_m = now - k * D
    if abs(next_p) > abs(next_m):
        now = next_m
    else:
        now = next_p
    visited.setdefault(str(now), 0)
    visited[str(now)] += 1
    if visited[str(now)] > 1:
        breaked = True
        break
    if left < 0:
        break
    # print(f"now:{now}")
if breaked:
    if left % 2 == 0:
        print(abs(now))
    else:
        print(abs(prev))
else:
    print(abs(now))
