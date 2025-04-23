# 生徒の人数
N = int(input())

# スコア格納のリスト
scores = [int(input()) for _ in range(N)]

# スコアとindexのペア
scores_with_index = [(score, i) for i, score in enumerate(scores)]
print(scores_with_index)  # [(55, 0), (57, 1), (55, 2), (52, 3)]

# スコアを基準に降順ソート
scores_with_index.sort(reverse=True, key=lambda x: x[0])
print(scores_with_index)  # [(57, 1), (55, 0), (55, 2), (52, 3)]

# 順位格納用のリスト
ranks = [0] * N
rank = 0

for i, (score, idx) in enumerate(scores_with_index):
    if i > 0 and score == scores_with_index[i - 1][0]:
        pass  # 同じランクを入れる
    else:
        rank = i + 1
    ranks[idx] = rank

# 1回目
# i=0, (57, 1) rank=1 ranks[1]=1

# 2回目
# i=1, (55, 0) score=55 前のスコア57 rank=2 ranks[0]=2

# 3回目
# i=2, (55, 2) score=55 前のスコア55 ranks=2 ranks[2]=2

# 4回目
# i=3, (52, 3) score=52 前のスコア55 ranks=
