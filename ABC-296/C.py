n, x = map(int, input().split())
A = list(map(int, input().split()))
B = set(A)

for a in A:
    if a + x in B:
        print("Yes")
        exit()
# A.sort()
#
# right = 0
#
# for left in range(n):
#     right = max(right, left)
#
#     while right < n and A[right] - A[left] <= x:
#         if A[right] - A[left] == x:
#             print("Yes")
#             exit()
#         right += 1
print("No")
