from bisect import bisect_left, bisect_right

n = int(input())
S = input()
W = list(map(int, input().split()))

adult = []
child = []

for i, s in enumerate(S):
    if s == "0":
        child.append(W[i])
    else:
        adult.append(W[i])

child.sort()
adult.sort()

candidate = set()
for w in W:
    candidate.add(w + 1)
    candidate.add(w - 1)

for c in set(adult) & set(child):
    candidate.discard(c)

ans = -1
for c in candidate:
    a = bisect_right(child, c)
    b = bisect_left(adult, c)
    ans = max(a + len(adult) - b, ans)

print(ans)
