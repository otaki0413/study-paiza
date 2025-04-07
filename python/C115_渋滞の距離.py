# N：車の数 M：渋滞の量
N, M = map(int, input().split())

# 渋滞の合計
total = 0
for _ in range(N - 1):
    distance = int(input())
    if distance <= M:
        total += distance

print(total)
