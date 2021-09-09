n, m = map(int, input().split())

A = [[] for _ in range(m)]
# ontop[x]: 色xのうちいちばんうえにあるボール
ontop = [[] for _ in range(n + 1)]

stack = []

for i in range(m):
    k = int(input())
    A[i] = list(map(int, input().split()))
    ontop[A[i]][-1].append(i)

    if ontop[A[i]][-2]
