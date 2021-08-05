N, K = map(int, input().split())

AB = []

for i in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

AB = list(sorted(AB, key=lambda x: x[0]))

dct = dict()
for ab in AB:
    a, b = ab[0], ab[1]
    dct[a] = dct.setdefault(a, 0) + b

now_i = 0
dict_keys = sorted(list(dct.keys()))


for dk in dict_keys:
    K -= 1
    now_i += 1
    if now_i <= dk <= now_i + K:
        K -= dk - now_i
        K += dct[dk]
        now_i = dk


if K > 0:
    now_i += K

print(now_i)


# now_i = 0
# while K > 0:
#     K -= 1
#     now_i += 1
#     if now_i in dct.keys():
#         K += dct[now_i]

# print(now_i)
