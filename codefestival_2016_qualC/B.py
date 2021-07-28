n, k = map(int, input().split())
A = list(map(int, input().split()))

if k == 1:
    print(n - 1)
    exit()

print(max(0, max(A) - 1 - (n - max(A))))
