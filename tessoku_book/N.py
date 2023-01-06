n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = set([a + b for a in A for b in B])
CD = set([a + b for a in C for b in D])
for a in AB:
    if k - a in CD:
        print("Yes")
        exit()
print("No")
