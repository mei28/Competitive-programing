from collections import deque,defaultdict
n = int(input())

Q = deque()

A = list(map(int,input().split()))

ans = 0
last_a = 1
for i in range(n):
    a = A[i]
    Q.append(a)
    print(Q,end=' ')
    if last_a == a:
        while len(Q)>=0:
            q = Q.pop()
            if q!=a:
                # もどす
                Q.append(q)
                break
    last_a  = a
    print(Q)
    print(len(Q))



