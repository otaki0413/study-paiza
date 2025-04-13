N = int(input())

# 必要な製品リスト
order_list = [i + 1 for i in range(N)]
# 存在カウント
exist_list = []

for i in range(N):
    x = int(input())
    if x in order_list:
        exist_list.append(x)

# 重複を削除したカウント
no_dup_count = len(set(exist_list))
# 不足分のカウント数
rest_count = len(order_list) - no_dup_count

print(rest_count)

# ----------------------------------------------------------

# 改善後
N = int(input())

# 必要な製品集合
required_products = set(range(1, N + 1))
# 届いた製品集合
received_products = set()

for _ in range(N):
    product = int(input())
    if product <= N:
        received_products.add(product)

missing_count = len(required_products - received_products)
print(missing_count)
