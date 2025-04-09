# N：折り紙の枚数, D：折り紙の1辺の長さ
N, D = map(int, input().split())

# 縦の長さ
height = D

# 横の長さ（つなぎ合わせ後）
width = D
for _ in range(N - 1):
    num = int(input())
    width += D - num

# 折り紙の面積
S = height * width
print(S)
