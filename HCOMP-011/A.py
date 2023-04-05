d, n = map(int, input().split())


# def make_divisors(n):
#     lower_divisors, upper_divisors = [], []
#     i = 1
#     while i * i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n // i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
#
#
# A = make_divisors(n)
#
# print(A[d + 1])

if n == 100:
    n += 1
print(str(n) + "00" * d)
