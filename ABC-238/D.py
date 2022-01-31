T = int(input())
A,S = [],[]
for _ in range(T):
    a,s = map(int,input().split())
    A.append(a)
    S.append(s)



for a,s in zip(A,S):
    t = s-2*a
    if t<0:
        print('No')
        continue

    if t& a==0:
        print('Yes')
    else:
        print('No')
