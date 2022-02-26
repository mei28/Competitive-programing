import bisect
q = int(input())

L = []

for i in range(q):
    tmp = list(input().split())
    _i = int(tmp[0])
    if _i == 1:
        x = int(tmp[1])
        bisect.insort_left(L,x)
    else:
        x = int(tmp[1])
        k = int(tmp[2])
        if _i==2:
            idx = bisect.bisect_right(L,x) 
            if idx-k<0:
                print(-1)
            else:
                print(L[idx-k])
            pass
        elif _i==3:
            idx =bisect.bisect_left(L,x) 
            if idx+k>len(L):
                print(-1)
            else:
                print(L[idx+k-1])
    

