x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)

P = P[:x]
Q = Q[:y]
R += P
R += Q

R.sort(reverse=True)
print(sum(R[: x + y]))
