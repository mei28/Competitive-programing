n = int(input())
A = list(map(int, input().split()))

grundy = 0
for a in A:
    grundy ^= a
print("First" if grundy else "Second")
