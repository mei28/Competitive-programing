n = int(input())
A = list(map(int,input().split()))

A = [a-i-1for i,a in enumerate(A)]

A.sort()
if len(A)%2==0:
    l,r = A[n//2],A[n//2+1]

    l_score = sum([abs(a-l) for a in A])
    r_score = sum([abs(a-r) for a in A])
    if l_score<r_score:
        print(l_score)
    else:
        print(r_score)

else:
    tmp = A[n//2]
    print(sum([abs(a-tmp) for a in A]))


