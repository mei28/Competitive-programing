n = int(input())
A = list(map(int, input().split()))

odd = A[1 : len(A) : 2]
even = A[0 : len(A) : 2]

if n % 2 == 0:
    ans = odd[::-1] + even
else:
    ans = even[::-1] + odd

print(*ans)
