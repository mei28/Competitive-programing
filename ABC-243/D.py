n,x = map(int,input().split())
S = list(input())
T = []

for c in S:
    if c=='U' and len(T)>0 and (T[-1]=="L" or T[-1]=="R"):
        T.pop()
    else:
        T.append(c)

for s in T:
    if s=="U":
        x//=2
    elif s=='R':
        x = 2*x+1
    elif s=="L":
        x=2*x

print(x)
