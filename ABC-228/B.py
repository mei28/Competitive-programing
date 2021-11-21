n, x = map(int, input().split())
A = [0] + list(map(int, input().split()))

ans = set()

while True:
    if x in ans or len(ans) == n:
        break
    ans.add(x)
    x = A[x]
print(len(ans))
