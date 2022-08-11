n = int(input())
A = list(map(int, input().split()))
B = [i + 1 for i in range(n)]

A.sort()
if A == B:
    print("Yes")
else:
    print("No")
