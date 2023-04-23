import random

n = int(input())

idx = random.choice([i + 1 for i in range(n)])
# sa = [i for i in range(0, n - 1, 2)]
#
# Qs = random.sample(sa, k=min(len(sa), 10))
#
# S = [2] * n
#
# for i in Qs:
#     print(f"? {i+1}", flush=True)
#     res = int(input())
#     S[i] = res
#     print(f"? {i+1+1}", flush=True)
#     res1 = int(input())
#     S[i + 1] = res1
#
#     if res != res1:
#         print(f"! {i + 1}")
#         exit()
#
# for i in range(n - 1):
#     if S[i] != 2 and S[i + 1] != 2 and S[i] != S[i + 1]:
#         print(f"! {i + 1}")
#         exit()
# print(f"! {ans}")
# exit()
