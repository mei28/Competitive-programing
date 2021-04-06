N = int(input())
A = list(map(int, input().split()))
all_ = sum(A)
S = [0] * len(A)

x = A[0]
y = sum(A[1:])
diff = abs(x - y)

for i in range(1, N - 1):
    x += A[i]
    y -= A[i]
    diff = min(diff, abs(x - y))

print(diff)
