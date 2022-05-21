n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_val = max(A)

for i, a in enumerate(A):
    if a == max_val:
        if i + 1 in B:
            print("Yes")
            exit()

print("No")
