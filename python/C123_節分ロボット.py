# 参加者の人数
N = int(input())

# 年齢と豆の数を管理する辞書作成
ages = {}
for i in range(N):
    age = int(input())
    ages[i] = {"age": age, "beans": 0}


# 命令の数
M = int(input())

for _ in range(M):
    start, end, count = map(int, input().split())
    for i in range(start - 1, end):
        person = ages[i]
        person["beans"] = min(person["beans"] + count, person["age"])


# 結果を出力
for i in range(N):
    print(ages[i]["beans"])
