N, L = map(int, input().split())
item_prices = list(map(int, input().split()))
max_price = max(item_prices)

amount: int = 0

for price in item_prices:
    if price == max_price and price >= L:
        price = int(price / 2)
    amount += price

print(amount)
