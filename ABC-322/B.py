n, m = map(int, input().split())
S = input()
T = input()

if S == T[:n] and S==T[-n:]:
    print(0)
elif S==T[:n]:
    print(1)
elif S==T[-n:]:
    print(2)
else:
    print(3)

