N = int(input())
flowers = input().split()
result_flowers = []

for f in flowers:
    if f not in result_flowers:
        result_flowers.append(f)

print(len(result_flowers))


# 集合(set)を使用して重複を自動削除する
N = int(input())
flowers = input().split()  # [1, 2, 1, 2, 1]
unique_flowers = set(flowers)  # set {1, 2}
print(len(unique_flowers))  # 2

# dict.fromKeysをリスト内包表記のパターン
N = int(input())
flowers = input().split()
result_flowers = list(dict.fromkeys(flowers))
print(len(result_flowers))
