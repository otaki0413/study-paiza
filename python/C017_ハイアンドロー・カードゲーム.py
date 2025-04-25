a, b = map(int, input().split())
n = int(input())

high_low_list = []
for _ in range(n):
    A, B = map(int, input().split())
    if a > A:
        text = "High"
    elif a < A:
        text = "Low"
    elif a == A and b > B:
        text = "Low"
    elif a == A and b < B:
        text = "High"
    else:
        pass
    high_low_list.append(text)

for text in high_low_list:
    print(text)


# ---------------------------------------------
# 別回答
def compare_cards(parent, child):
    parent_a, parent_b = parent
    child_a, child_b = child

    if parent_a > child_a:
        return "High"
    elif parent_a < child_a:
        return "Low"
    else:
        return "Low" if parent_b > child_b else "High"


# 親カードの入力
a, b = map(int, input().split())
parent_card = (a, b)

# 子カードの数の入力
n = int(input())

# 各子カードとの比較結果を格納
results = []
for _ in range(n):
    child_a, child_b = map(int, input().split())
    result = compare_cards(parent_card, (child_a, child_b))
    results.append(result)

# 結果の出力
for result in results:
    print(result)
