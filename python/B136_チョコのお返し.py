# 入力
N, H, W = map(int, input().split())
sy, sx = map(int, input().split())
s = input()

# チョコレートmapの読み取り
chocolates = [list(map(int, input().split())) for _ in range(H)]

# 移動の方向を定義
directions = {
    "F": (-1, 0),
    "B": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


# Pythonのリストは0-indexedなので座標も調整
y, x = sy - 1, sx - 1

# 結果を保存
results = []

# 1ステップずつ移動
for move in s:
    dy, dx = directions[move]
    y += dy
    x += dx
    results.append(chocolates[y][x])

# 出力
for choco in results:
    print(choco)
