import sys
from itertools import combinations
from operator import add


l = []
with open(sys.argv[1], "r") as f:
    for s_line in f:
        # 改行コードの除去
        s_line = s_line.replace("\n", "")
        l.append(s_line)

key_set = set()
value_set = set()

for i in l:
    k, vs = i.split(":")
    key_set.add(k)
    vs = list(vs.split())
    for v in vs:
        value_set.add(v)


# マッピングする
# str -> int
key_map = {}
# int -> str
key_remap = {}
# str -> int
value_map = {}
# int -> str
value_remap = {}
k_i = 0
for k in key_set:
    key_map[k] = k_i
    key_remap[k_i] = k
    k_i += 1
v_i = 0
for v in value_set:
    value_map[v] = v_i
    value_remap[v_i] = v
    v_i += 1

# 行: 料理名，　列:使う食材
table = [[0 for _ in range(len(value_set))] for _ in range(len(key_set))]

for i in l:
    k, vs = i.split(":")
    vs = vs.split()
    for v in vs:
        table[key_map[k]][value_map[v]] = 1

# すべて組み合わせる
for i in range(1, len(key_set) + 1):
    # i: nCi
    comb = list(combinations(key_set, i))
    cnt_list = [0] * len(value_set)
    menu_set = set()
    for j in comb:
        # j:組み合わせの1つのパターン
        for k in j:
            # k: 1パターンないの1料理
            use_list = table[key_map[k]]
            cnt_list = list(map(add, cnt_list, use_list))

        if all([a == 1 for a in cnt_list]):
            # TODO: 全ての食材を使用するときまでしか列挙できていない
            print(", ".join(j))
        # カウントの初期化
        cnt_list = [0] * len(value_set)
