import itertools


def apply_function(A, B, x):
    return A * x + B


def max_value(N, K, A, B):
    max_result = float("-inf")

    for comb in itertools.combinations(range(N), K):
        for perm in itertools.permutations(comb):
            x = 1
            for i in perm:
                x = apply_function(A[i], B[i], x)
            max_result = max(max_result, x)

    return max_result


N, K = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

print(max_value(N, K, A, B))
