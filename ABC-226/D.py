from itertools import combinations
N = int(input())
xy = [tuple(map(int,input().split())) for _ in range(N)]

from math import gcd
setA=set()
for p1,p2 in combinations(xy,2):
    x1,y1=p1
    x2,y2=p2
    dx=abs(x1-x2); dy=abs(y1-y2)
    if dx==0 or dy==0:
        g=max(abs(dx),abs(dy))
        setA.add(  ((x1-x2)//g,(y1-y2)//g)  )
        setA.add(  ((x2-x1)//g,(y2-y1)//g)  )
    else:
        g=gcd(dx,dy)
        setA.add(  ((x1-x2)//g,(y1-y2)//g))
        setA.add(  ((x2-x1)//g,(y2-y1)//g))
print(len(setA))


# = int(input())
# = map(int,input().split())
# = list(map(int,input().split()))
# = input().split()
