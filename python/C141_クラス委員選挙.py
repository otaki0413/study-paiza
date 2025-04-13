# N = int(input())

# # 各名前のカウント数を保持する辞書
# names = {}

# # 辞書格納
# for _ in range(N):
#     name = input()
#     if name in names:
#         names[name] += 1
#     else:
#         names[name] = 1

# # 値が最大となるkey, value取得
# max_key, max_value = max(names.items(), key=lambda x: x[1])
# print(max_key)


# # 処理をもっとシンプルにするパターン
# N = int(input())

# # 各名前のカウント数を保持する辞書
# votes = {}

# # 投票カウント
# for _ in range(N):
#     name = input()
#     votes[name] = votes.get(name, 0) + 1

# # 最多投票者を取得
# winner = max(votes, key=votes.get)

names = ["田中", "佐藤", "田中", "山本", "佐藤"]
name_counts = {}

for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

print(name_counts)  # {'田中': 3, '佐藤': 3, '山本': 2}
