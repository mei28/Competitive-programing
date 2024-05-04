def min_good_index_distance(n, k, p):
    from collections import defaultdict, deque

    # 各値がどこに現れるかを記録する辞書
    pos = defaultdict(deque)
    for idx, val in enumerate(p):
        pos[val].append(idx)

    min_distance = float("inf")

    # 考慮すべき全ての値の範囲を調べる
    for start in range(1, n - k + 2):
        valid = True
        max_idx = -1
        min_idx = float("inf")

        # 連続するK個の整数が全て存在するかを確認
        for num in range(start, start + k):
            if not pos[num]:  # num が存在しなければ、その組は無効
                valid = False
                break
            # 最小インデックスと最大インデックスを更新
            max_idx = max(max_idx, pos[num][0])
            min_idx = min(min_idx, pos[num][0])
            pos[num].popleft()  # 次に同じ数を使うために最初の要素を削除

        if valid:
            # 有効な組が見つかれば、最小距離を更新
            min_distance = min(min_distance, max_idx - min_idx)

    return min_distance


# 入力として数値を受け取る
n, k = map(int, input().split())
p = list(map(int, input().split()))

# 関数を呼び出して解を求める
print(min_good_index_distance(n, k, p))
