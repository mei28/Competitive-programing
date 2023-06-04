MOD = 998244353


def count_shifts(n, s):
    groups = []
    count = 0
    current_group = None

    # シフト表の連続した出勤日と欠勤日のグループを数える
    for i in range(n):
        if s[i] == "#":
            if current_group is None:
                current_group = "#"
            elif current_group == "#":
                current_group += "#"
        else:
            if current_group is None:
                current_group = "."
            elif current_group == ".":
                current_group += "."
            else:
                groups.append(len(current_group))
                current_group = None
                count += 1

    if current_group is not None:
        groups.append(len(current_group))
        count += 1

    ans = 1
    group_count = {}

    # 各グループの長さをカウントする
    for length in groups:
        if length not in group_count:
            group_count[length] = 0
        group_count[length] += 1

    # 青木君のシフト表として考えられるものの個数を計算する
    for m in range(1, n + 1):
        if n % m == 0:
            if m in group_count:
                x = group_count[m]
                ans = (ans * pow(2, x, MOD)) % MOD
                group_count.pop(m)

            for length, count in group_count.items():
                if (n // m) % length == 0:
                    y = count * (n // m) // length
                    ans = (ans * pow(2, y, MOD)) % MOD

    return ans


# 入力の読み込み
n = int(input())
s = input()

# 青木君のシフト表として考えられるものの個数を求める
result = count_shifts(n, s)

# 結果を出力
print(result)
