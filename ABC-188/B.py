n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for a,b in zip(A,B):
    ans += a*b

if ans==0:
    print('Yes')
else:
    print('No')
