def calculate_cost(operations):
    # 操作のリストに基づいてコストを計算する
    return sum(len(op[1]) for op in operations)


def get_neighbors(piles):
    # 全ての合法的な移動を試みる
    neighbors = []
    for i, pile_i in enumerate(piles):
        for j, pile_j in enumerate(piles):
            if i != j and pile_i:  # 異なる山間で移動が可能
                # 最小の番号の箱を移動する必要がある
                min_box = min(pile_i)
                min_box_idx = pile_i.index(min_box)
                # その上の全ての箱を移動させる
                to_move = pile_i[min_box_idx:]
                # 新しい状態を作成
                new_piles = [p[:] for p in piles]
                new_piles[j].extend(to_move)
                new_piles[i] = new_piles[i][:min_box_idx]
                # 移動した箱の数を操作として記録
                operation = (i, to_move, j)
                neighbors.append((new_piles, [operation]))
    return neighbors


def is_goal_state(piles):
    # 全ての箱が正しい順序で運び出されているか確認する
    return all(pile == sorted(pile) for pile in piles)


def beam_search(piles, beam_width):
    beam = [([], piles)]  # (operations, piles)

    while beam:
        next_beam = []
        for operations, piles in beam:
            if is_goal_state(piles):
                return operations  # ゴール状態に到達した場合は操作を返す
            for new_piles, operation in get_neighbors(piles):
                next_operations = operations + operation
                next_beam.append((next_operations, new_piles))

        # コストが最小の状態のみをビームに保持
        next_beam.sort(key=lambda x: calculate_cost(x[0]))
        beam = next_beam[:beam_width]

    return []  # ゴールに到達できなかった場合は空のリストを返す


# 初期状態の入力を取得
n, m = map(int, input().split())  # n: 箱の数, m: 山の数
initial_piles = [list(map(int, input().split())) for _ in range(m)]

# ビームサーチを実行し、結果を表示
operations = beam_search(initial_piles, 5)
if operations:
    print("Operations to reach the goal state:")
    for op in operations:
        print(op)
else:
    print("No solution found with the given beam width.")
