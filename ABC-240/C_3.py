n, x = map(int,input().split())
dp = [False] * 100000000

A,B = [],[]
AB = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    AB.append((a,b))

AB = list(sorted(AB,key=lambda x:x[0]))







