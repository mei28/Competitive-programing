n = int(input())
ans = ""
while n > 0:
    ans += str(n % 2)
    n //= 2
print(f"{ans[::-1]:>010}")
