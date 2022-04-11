import sys
sys.setrecursionlimit(99999)

n = int(input())

S = [""]*20
S[1] = '1'

def rec(i:int):
    if S[i] != '':
        return S[i]
    if i==1:
        return '1'
    S[i] = S[i-1] +" " +str(i)+' ' +S[i-1] 
    return S[i]

for i in range(1,n+1):
    rec(i)
print(''.join(S[n]))
