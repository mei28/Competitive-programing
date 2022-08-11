n, k = map(int, input().split())
C = list(map(int, input().split()))

counter = set(C[:k])


ans = -1
for i in range(k, n):
    left = C[i - k]
    right = C[i]
    if left in counter:
        counter.remove(left)
    counter.add(right)
    ans = max(ans, len(counter))
print(ans)
