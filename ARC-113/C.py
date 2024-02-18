from collections import defaultdict

S = input()
n = len(S)
result = 0

cnt = defaultdict(int)

# 前の文字と、前の前の文字
prev_c, prev2_c = "", ""

for i in range(len(S) - 1, -1, -1):
    now_c = S[i]

    # 前と違う文字が二回連続で現れたら
    if now_c == prev_c != prev2_c:
        # そこから右がその文字に書き換えられるので、
        # 該当文字を除く文字数を答えに加算。
        result += (n - i - 1) - cnt[now_c]
        # カウントは全て書き変わった文字になる
        cnt = defaultdict(int, {now_c: len(S) - i - 1})
    cnt[now_c] += 1
    prev2_c, prev_c = prev_c, now_c

print(result)
