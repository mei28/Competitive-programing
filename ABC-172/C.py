n,m,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ok = 0
ng = n+m+1

_A = [0]*(n+1)
_B = [0]*(m+1)

for i in range(n):
    _A[i+1] = _A[i]+A[i]
for i in range(m):
    _B[i+1] = _B[i]+B[i]

ans = 0
ok = m

for a in range(n+1):
    while 0<= ok and k<_A[a]+_B[ok]:
        ok-=1;
    if 0<=ok:
        ans = max(ans,a+ok)

print(ans)
