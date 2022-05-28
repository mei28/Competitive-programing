a, b, c = map(int, input().split())
A = [a, b, c]
A.sort()

if A[1] == b:
    print("Yes")
else:
    print("No")
