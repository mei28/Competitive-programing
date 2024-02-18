N = int(input())
A = [0] * (2 * N)
for i in range(2 * N - 1):
    A[i] = list(map(int, input().split()))

ans = 0


def calc(dancer, score):
    if len(dancer) == 0:
        global ans
        ans = max(ans, score)
        return
    last = dancer[-1]
    for i in range(len(dancer) - 1):
        other = dancer[i]
        calc(dancer[:i] + dancer[i + 1 : -1], score ^ A[other][last - other - 1])


calc(list(range(2 * N)), 0)
print(ans)
