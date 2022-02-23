from collections import deque

n, x = map(int, input().split())

Q = [0]
for i in range(n):
    a, b = map(int, input().split())
    old_Q = Q.copy()
    Q = []
    for q in old_Q:
        Q.append(q + a)
        Q.append(q + b)

ans = set(Q)

# print(ans)
print("Yes" if x in ans else "No")
