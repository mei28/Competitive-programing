import sys 
sys.setrecursionlimit(99999)

n = int(input())

def dfs(s:str):
    if int(s)>n:
        return 0

    ret = 0
    if all(s.count(c)>0 for c in '753'):
        ret = 1

    for c in '753':
        ret += dfs(s+c)

    return ret

print(dfs('0'))


