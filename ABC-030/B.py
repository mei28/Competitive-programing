n, m = map(int, input().split())

m_angle = m * 6

if n >= 12:
    n -= 12
n_angle = n * 30 + m * 0.5

ans = abs(n_angle - m_angle)

print(ans if ans <= 180 else 360 - ans)
