# from math import sin, cos, pi

# n = int(input())

# x0, y0 = map(int, input().split())
# x1, y1 = map(int, input().split())


# a = x0 + y0 * 1j
# b = x1 + y1 * 1j

# offset = (a + b) / 2
# a -= offset
# b -= offset

# ans = a * (cos(2 * pi / n) + sin(2 * pi / n) * 1j)
# ans += offset


# print(ans.real, ans.imag)

from math import sin, cos, pi

n = int(input())

x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())

a = x0 + y0 * 1j
b = x1 + y1 * 1j

offset = (a+b)/2

ans = a*(cos(2*pi/n)+sin(2*pi/n)*1j)
ans += offset
print(ans.real, ans.imag)

