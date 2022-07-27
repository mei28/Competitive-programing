n = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i,n):
        if i == j:
            continue
        ans += D[i] * D[j]

print(ans)
