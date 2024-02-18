n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

candidates = set()
for i in range(1):
    for j in range(n):
        candidates.add(A[i] ^ B[j])


ans = []

A.sort()
B.sort()


def ok(e: int) -> bool:
    b2 = []
    for i in range(n):
        b2.append(A[i] ^ e)

    b2.sort()
    return B == b2


for e in candidates:
    if ok(e):
        ans.append(e)

ans.sort()
print(len(ans))
for a in ans:
    print(a)
