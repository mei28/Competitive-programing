from collections import defaultdict


def main():
    N = int(input())
    Q = int(input())
    boxes = [defaultdict(int) for _ in range(N)]
    num_to_box = defaultdict(set)

    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            i, j = query[1], query[2] - 1
            boxes[j][i] += 1
            num_to_box[i].add(j)

        elif query[0] == 2:
            i = query[1] - 1
            for num, count in sorted(boxes[i].items()):
                for _ in range(count):
                    print(num, end=" ")
            print()

        else:
            i = query[1]
            for box_idx in sorted(num_to_box[i]):
                print(box_idx + 1, end=" ")
            print()


if __name__ == "__main__":
    main()
