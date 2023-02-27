n = int(input())
X = list(map(int, input().split()))
X.sort()
A = X[n:-(n)]

print(sum(A) / len(A))
