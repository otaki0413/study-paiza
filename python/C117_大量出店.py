# 店数(N)
# 1杯あたりの利益(C)× 販売数(?) - 建設費用(A) - 人件費(B) × 営業期間(M)
N, M = map(int, input().split())
A, B, C = map(int, input().split())

# 閉店予定の店数
closing_count: int = 0

for _ in range(N):
    sell_count = int(input())
    benefit = (C * sell_count) - A - (B * M)
    if benefit < 0:
        closing_count += 1

print(closing_count)
