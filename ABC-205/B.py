n = map(int, input().split())
A = list(map(int, input().split()))
A_s = set(A)

if len(A_s) == len(A):
    print("Yes")
else:
    print("No")
