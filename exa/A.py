from typing import List, Set

if __name__ == "__main__":
    W: str = input()
    L: List[str] = input().split()
    w_set: Set[chr] = set(W)
    ans: Set[chr] = set()

    for l in L:
        l_set: Set[chr] = set(l)
        if l_set == w_set:
            ans.add(l)
    print(len(ans))
