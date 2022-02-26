from collections import Counter
n, m = map(int,input().split())

A = Counter(list(map(int,input().split())))
B = Counter(list(map(int,input().split())))

for kb,vb in B.items():
    if vb>A[kb]:
        print('No')
        exit()

print('Yes')

    
