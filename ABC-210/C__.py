from collections import Counter

n, k = map(int, input().split())
C = list(map(int, input().split()))

counter = Counter(C[:k])
ans = len(counter)

for i in range(k, n):
    left = C[i - k]
    right = C[i]
    counter[left] -= 1
    counter[right] += 1

    if counter[left] == 0:
        del counter[left]
    ans = max(ans, len(counter))
print(ans)
