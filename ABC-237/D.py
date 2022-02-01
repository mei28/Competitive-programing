from collections import deque
n = int(input())
S = input()

Q = deque()
Q.append(n)

for i in range(n-1,-1,-1):
    if S[i]=='L':
        Q.append(i)
    else:
        Q.appendleft(i)


print(*Q)
