import itertools
import sys
sys.setrecursionlimit(99999)
n,x = map(int,input().split())



AB = []
for i in range(n):
    a,b = map(int,input().split())
    AB.append((a,b))

ans = set()
def dfs(A,i):
    if len(A)==n:
        ans.add(sum(A))
        return 

    for v in AB[i]:
        A.append(v)
        dfs(A,i+1)
        A.pop()

dfs([],0)

if x in ans:
    print('Yes')
else:
    print('No')

