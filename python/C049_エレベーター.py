# 定数
INITIAL_FLOOR = 1


# エレベーターの総移動回数を算出する関数
def calc_total_floor_movement(moves: list[int]) -> int:
    current_floor = INITIAL_FLOOR
    total_floor_movement = 0
    for floor in moves:
        total_floor_movement += abs(current_floor - floor)
        current_floor = floor
    return total_floor_movement


N = int(input())
floor_moves = [int(input()) for _ in range(N)]

result = calc_total_floor_movement(floor_moves)
print(result)
