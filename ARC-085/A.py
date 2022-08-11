n, m = map(int, input().split())

time = (1900 * m + 100 * (n - m)) * (1 << m)
print(time)
