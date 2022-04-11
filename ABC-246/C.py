
n,k,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)

ans  = sum(A)

m=0

for a in A: 
    m+= a//x
m = min(m,k)

ans -= m*x
k-= m

for i in range(n):
    A[i] %= x

A.sort()

for i in range(n-1,-1,-1):
    if k==0:break
    ans -= A[i]
    k-=1

print(ans)

