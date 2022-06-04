n, m = map(int, input().split())

# print((10 ** n) // m % m)
ans = pow(10, n, m * m)
ans //= m
ans %= m
print(ans)
