A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

if A[0] == B[0]:
    if C[1]==A[1]:
        print(C[0],B[1])
    else:
        print(C[0],A[1])
elif A[0] == C[0]:
    if B[1] == A[1]:
        print(B[0],C[1])
    else:
        print(B[0],A[1])

else:
    if A[1]==B[1]:
        print(A[0],C[1])
    else:
        print(A[0],B[1])
