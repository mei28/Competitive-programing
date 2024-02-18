import heapq


def min_operations(nums):
    min_heap = nums[:]  # 最小ヒープ
    max_heap = [-num for num in nums]  # 最大ヒープ
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    operations = 0
    while True:
        max_val = -heapq.heappop(max_heap)  # 最大値を取得
        min_val = heapq.heappop(min_heap)  # 最小値を取得

        # 最小値と最大値の差が1以下なら終了
        if max_val - min_val <= 1:
            break

        # それ以外の場合、最小値を1増やし、最大値を1減らす
        diff = (max_val - min_val) // 2
        heapq.heappush(min_heap, min_val + diff)
        heapq.heappush(max_heap, -(max_val - diff))

        operations += diff

    return operations


n = int(input())
A = list(map(int, input().split()))

print(min_operations(A))
