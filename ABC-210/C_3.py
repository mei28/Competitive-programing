from collections import Counter

n,k = map(int,input().split())
C = list(map(int,input().split()))

cnter = Counter(C[:k])
ans = len(cnter)

for i in range(k,n):
    left = C[i-k]
    right = C[i]

    cnter[left]-=1
    cnter[right]+=1

    if cnter[left] ==0:
        del cnter[left]
    ans = max(ans, len(cnter))

print(ans)
