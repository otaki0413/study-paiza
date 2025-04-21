N, D = map(int, input().split())
X, Y = map(int, input().split())

count = 0
for _ in range(N):
    target_x, target_y = map(int, input().split())
    distance = abs(X - target_x) + abs(Y - target_y)
    if distance <= D:
        count += 1

print(count)

# ---
# 別回答
from typing import Tuple, List


def calculate_manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """
    2点間のマンハッタン距離を計算する

    Args:
        p1 (Tuple[int, int]): 点1の座標
        p2 (Tuple[int, int]): 点2の座標

    Returns:
        int: マンハッタン距離
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def count_reachable_houses(
    paiza_house: Tuple[int, int], houses: List[Tuple[int, int]], max_distance: int
) -> int:
    """
    訪問可能な家の数を計算する

    Args:
        paiza_house (Tuple[int, int]): PAIZAさんの家の座標
        houses (List[Tuple[int, int]]): 全ての家の座標リスト
        max_distance (int): 最大訪問可能距離

    Returns:
        int: 訪問可能な家の数
    """
    return sum(
        1
        for house in houses
        if calculate_manhattan_distance(paiza_house, house) <= max_distance
    )


def main():
    """メイン処理"""
    # 入力処理
    N, D = map(int, input().split())
    X, Y = map(int, input().split())
    houses = [tuple(map(int, input().split())) for _ in range(N)]

    # 訪問可能な家の数を計算
    result = count_reachable_houses((X, Y), houses, D)
    print(result)


if __name__ == "__main__":
    main()
