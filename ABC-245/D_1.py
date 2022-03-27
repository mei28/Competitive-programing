from numpy import poly1d

n,m = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

polyA = poly1d(list(A[::-1]))
polyC = poly1d(list(C[::-1]))

polyB = polyC/polyA

coefB = list(map(int,polyB[0].c))

ans = list(coefB[::-1])

print(*ans)
