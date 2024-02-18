n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))

q = int(input())
ans = []
for i in range(q):
    r, c = map(lambda x: int(x) - 1, input().split())
    if R[r] + C[c] >= n + 1:
        ans.append("#")
    else:
        ans.append(".")

print(*ans, sep="")
