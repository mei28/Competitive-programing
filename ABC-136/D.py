def solve(s: str) -> int:
    n = len(s)
    ans = [0] * (n)
    cnt = 0
    for i, moji in enumerate(s):
        if moji == "R":
            cnt += 1
            continue
        else:
            even_num = cnt // 2  # 折返し地点までの距離が偶数の人の数
            odd_num = cnt - even_num  # 折返し地点までの距離が奇数の人の数
            ans[i] += even_num  # 折返し地点までの距離が偶数の人は、ans[i]に収束する
            ans[i - 1] += odd_num  # 折返し地点までの距離が奇数の人は、ans[i-1]に収束する
            cnt = 0

    # Lグループについて考える
    cnt = 0  # Lグループの人数
    for i in range(n - 1, -1, -1):
        if s[i] == "L":
            cnt += 1
            continue
        else:
            even_num = cnt // 2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i + 1] += odd_num
            cnt = 0

    return ans


if __name__ == "__main__":
    s = input()
    print(*solve(s))
