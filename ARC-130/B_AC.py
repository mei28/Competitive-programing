# import sys

# H, W, C, Q = map(int, sys.stdin.readline().split())
# m = map(int, sys.stdin.read().split())
# query = tuple(zip(m, m, m))

# ANS = [0] * (C + 1)
# done_1 = set()
# done_2 = set()

# # 後ろから処理して絶対に塗られない位置を考える
# for t, n, c in query[::-1]:
#     if t == 1:
#         done_1.add(n)
#         # 上から被らされる個数だけ引かれる
#         ANS[c] += W - len(done_2)

#     if t == 2 and n not in done_2:
#         done_2.add(n)
#         # 上から被らされる個数だけ引かれる
#         ANS[c] += H - len(done_1)

# print(*ANS[1:])
import sys

H, W, C, Q = map(int, sys.stdin.readline().split())
m = map(int, sys.stdin.read().split())
query = tuple(zip(m, m, m))

ANS = [0] * (C + 1)
done_1 = set()
done_2 = set()

for t, n, c in query[::-1]:
  if t == 1 and n not in done_1:
    done_1.add(n)
    ANS[c] += W - len(done_2)
  if t == 2 and n not in done_2:
    done_2.add(n)
    ANS[c] += H - len(done_1)

print(*ANS[1:])
