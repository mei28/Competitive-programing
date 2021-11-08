n = int(input())
A = list(map(int,input().split()))

B = 0
for a in A:
    B ^= a

ans = []
for a in A:
    ans.append(B^a)

print(*ans)
