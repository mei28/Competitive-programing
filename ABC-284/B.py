t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print(sum([a % 2 == 1 for a in A]))
