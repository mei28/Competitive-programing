N,A,B=map(int,input().split())

if A>B:
    print(0)
    exit()
if N==1 and A==B:
    print(1)
    exit()
if N==1 and A!=B:
    print(0)
    exit()
print((N-2)*(B-A)+1)





