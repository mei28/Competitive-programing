n = int(input())
S = []
T = []
ST = []

for _ in range(n):
    s, t = input().split()
    S.append(s)
    T.append(t)
    ST.append([s, t])

if set(S) == set(T):
    print("No")
else:
    print("Yes")
